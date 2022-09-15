from django import template
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django_dramatiq.models import Task

from src.services.base.baseimport import BaseImport
from src.apps.common.dataclasses import ETL
from src.config import settings

from .forms import ConnectWrapperForm
from .filters import (
    PipelineListFilter, ConnectTypeListFilter, PipelineTablesListFilter,
    PipelineStatusListFilter,
)
from .validators import SQLConnectValidator, DBFConnectValidator
from .models import ConnectWrapper, ConnectSet, ImportTables, MSSQL_ENGINE

# Register your models here.

register = template.Library()


# ref https://stackoverflow.com/questions/45676500/django-admin-actions-on-single-object
class ImportTablesAdmin(admin.ModelAdmin):
    list_display = (
        'source_table',
        'dest_table',
        'uploadable',
        'show_result',
        'upload_record',
        # 'run_export',
        # 'run_import',
        'run_export_import',
    )
    readonly_fields = (
        'message_id',
        'redis_message_id',
        'last_write',
        'upload_record',
    )
    list_filter = (PipelineTablesListFilter, PipelineStatusListFilter)
    # list_filter = ('connects__name',)
    search_fields = ('source_table',)
    # list_editable = ('uploadable',)
    # save_on_top = True



    def has_add_permission(self, request):
        return False


    @admin.display(description=_('Export'))
    def run_export(self, obj):
        return self.create_link(obj, ETL.MODE.EXPORT)


    @admin.display(description=_('Import'))
    def run_import(self, obj):
        return self.create_link(obj, ETL.MODE.IMPORT)


    @admin.display(description=_('Export/Import'))
    def run_export_import(self, obj):
        return self.create_link(obj, ETL.MODE.FULL)


    @admin.display(description=_('Task status'))
    def show_result(self, obj):
        define_color = '#B15117'
        status = mark_safe(f'<span style="color: {define_color};">'
                                f'{_("Unknown") if obj.uploadable else "-"}'
                           f'</span>'
                           )
        if obj.message_id:
            # Highlight the font in color if status not equal Done
            is_done = _('Done')
            result = Task.tasks.filter(pk=obj.message_id).get()
            if result:
                status = result.status.title()
                url = reverse('admin:django_dramatiq_task_change', args=[result.pk])
                return mark_safe(
                    f'<a href="{url}" class="historylink">'
                        f'<span style="color: {define_color};">{status}'
                    f'</span></a>' \
                        if status != is_done else \
                    f'<a href="{url}" class="historylink">{status}</a>'
                )
        return status

    def create_link(self, obj, mode):
        if obj.uploadable:
            url = reverse(f'{ETL.URLNAME.EXPORT_SINGLE_TABLE}', kwargs={'table_pk': obj.pk, 'mode': mode})
            return mark_safe(f'<a href="{url}" class="historylink">Run</a>')


class ConnectSetAdmin(admin.ModelAdmin):
    validate_form = None
    ordering = ('-name',)

    list_display = (
        'name',
        # 'source_conection',
        # 'dest_conection',
        'enabled',
        # 'create_tables_actions',
        # 'run_export',
        # 'run_import',
        'run_export_import',
    )
    list_filter = (PipelineListFilter,)
    save_on_top = True

    def save_form(self, request, form, change):
        # Check connections
        type = form.cleaned_data['type']
        list_pk = [pk for pk in [form.cleaned_data['source_conection'].pk, form.cleaned_data['dest_conection'].pk]]

        for connect_pk in list_pk:
            connect = ConnectWrapper.objects.filter(pk=connect_pk).get()

            if connect.engine == MSSQL_ENGINE:
                self.validate_form = SQLConnectValidator(request, connect, change, type)
            else:
                self.validate_form = DBFConnectValidator(request, connect, change, type)

            self.validate_form.validate()

        return super(ConnectSetAdmin, self).save_form(request, form, change)


    def save_model(self, request, obj, form, change):
        super(ConnectSetAdmin, self).save_model(request, obj, form, change)
        self.create_or_update_import_tables_list(request=request, object_pk=obj.pk)


    @admin.display(description=_('Export'))
    def run_export(self, obj):
        return self.create_link(obj, ETL.MODE.EXPORT)


    @admin.display(description=_('Import'))
    def run_import(self, obj):
        return self.create_link(obj, ETL.MODE.IMPORT)


    @admin.display(description=_('Export/Import'))
    def run_export_import(self, obj):
        return self.create_link(obj, ETL.MODE.FULL)

    # run_import.short_description = 'Import'
    run_import.allow_tags = True

    def create_link(self, obj, mode):
        connsets = self.model.consets.record(obj.pk)
        if connsets.enabled:
            url = reverse(f'{ETL.URLNAME.PIPELINE_EXPORT_IMPORT}', kwargs={'poll_pk': obj.pk, 'mode': mode})
            link = mark_safe(f'<a href="{url}" class="historylink">Run</a>')
        else:
            # link = mark_safe(f'<a href="#" class="historylink">Disable</a>')
            link = ''

        return link

    # def get_urls(self):
    #     urls = super().get_urls()
    #     custom_urls = [
    #         re_path(
    #             r'^(?P<object_pk>.+)/create-tables-list/$',
    #             self.admin_site.admin_view(self.create_or_update_import_tables_list),
    #             name='create-table-list',
    #         ),
    #     ]
    #     return custom_urls + urls


    # def create_tables_actions(self, obj):
    #     return format_html(
    #         '<a class="button" href="{}">Create or Update</a>&nbsp;',
    #         reverse('admin:create-table-list', args=[obj.pk]),
    #     )
    #
    # create_tables_actions.short_description = 'Create table list'
    # create_tables_actions.allow_tags = True


    def create_or_update_import_tables_list(self, request, object_pk, *args, **kwargs):
        import_class = BaseImport()
        poll = ConnectSet.consets.record(pk=object_pk)
        prefix = settings.PIPE_MODULES[poll.type]['table_prefix']

        if len(ImportTables.tables.filter(connects=object_pk).all()) == 0:

            table_list = import_class.get_list_tables_from_model_class(
                settings.PIPE_MODULES[poll.type]['export'], 'models'
            )

            for table in table_list:
                ImportTables.tables.update_or_create(
                    source_table=table.upper(),
                    dest_table=f"{prefix}{table.upper()}",
                    connects_id=poll.pk
                )
            messages.success(request, f'The import tables list for {poll.name} connection has successfully added!')
        else:
            messages.warning(request, f'The {poll.name} connection has already tables list for import')
        # reverse('admin:<yourapp>_<yourmodel>_change', args=[object_pk])
        # Page	URL name	Parameters
        # Changelist	{{ app_label }}_{{ model_name }}_changelist
        # Add	{{ app_label }}_{{ model_name }}_add
        # History	{{ app_label }}_{{ model_name }}_history	object_id
        # Delete	{{ app_label }}_{{ model_name }}_delete	object_id
        # Change	{{ app_label }}_{{ model_name }}_change	object_id
        return HttpResponseRedirect(
            reverse('admin:core_connectset_changelist')
        )


class ConnectWrapperAdmin(admin.ModelAdmin):
    # validate_form = None

    list_display = ('conname', 'engine', 'is_active')
    fieldsets = (
        (None, {
            'fields': ('conname', 'engine', 'description', 'is_active',),
            'classes': ('predefined',)
        }),
        ('Database', {
            'fields': ('name', 'options',)
        }),
        ('Security', {
            'fields': ('user', 'password', 'host', 'port'),
            'classes': ('security_fieldset',)
        }),
    )
    list_filter = (ConnectTypeListFilter,)
    search_fields = ('conname',)
    exclude = ['slug_name',]
    save_as = True
    save_on_top = True

    form = ConnectWrapperForm

    class Media:
        js = ('dropdown/js/base.js',)

    # change_form_template = 'admin/core/custom_change_form.html'


    def save_form(self, request, form, change):
        # if form.cleaned_data["engine"] == MSSQL_ENGINE:
        #     self.validate_form = SQLConnectValidator(request, form, change)
        # else:
        #     self.validate_form = DBFConnectValidator(request, form, change)
        #
        # self.validate_form.validate()

        return super(ConnectWrapperAdmin, self).save_form(request, form, change)


    def delete_model(self, request, obj):
        self.validate_class.drop_database()
        super(ConnectWrapperAdmin, self).delete_model(request, obj)

    # def get_changeform_initial_data(self, request):
    #     initial = super(ConnectWrapperAdmin, self).get_changeform_initial_data(request)
    #     return initial


    # def response_change(self, request, obj):
    #     opts = self.model._meta
    #     pk_value = obj._get_pk_val()
    #     preserved_filters = self.get_preserved_filters(request)
    #
    #     if not self._change:
    #         self.create_database()
    #     else:
    #         try:
    #             if self.database_exists() is None:
    #                 self.create_database()
    #                 messages.info(request, "%s" % _(f"Database {self.DATABASE_NAME} was successful created."))
    #         except Exception as e:
    #             if not self._show_error_message(request, e):
    #                 raise
    #         # success = self._check_connection(request)
    #
    #
    #     if "_customaction" in request.POST:
    #         # handle the action on your obj
    #         redirect_url = reverse('admin:%s_%s_change' %
    #                                (opts.app_label, opts.model_name),
    #                                args=(pk_value,),
    #                                current_app=self.admin_site.name)
    #         redirect_url = add_preserved_filters({'preserved_filters': preserved_filters, 'opts': opts}, redirect_url)
    #         return HttpResponseRedirect(redirect_url)
    #
    #     else:
    #         return super(ConnectWrapperAdmin, self).response_change(request, obj)



admin.site.register(ImportTables, ImportTablesAdmin)
admin.site.register(ConnectSet, ConnectSetAdmin)
admin.site.register(ConnectWrapper, ConnectWrapperAdmin)

admin.site.site_header = _("DBF to MSSQL Uploader")