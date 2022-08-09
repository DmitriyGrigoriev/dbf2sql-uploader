from django import template
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_dramatiq.models import Task
from .models import ConnectWrapper, ConnectSet, ImportTables, MSSQL_ENGINE
from .forms import ConnectWrapperForm
from .classes import SQLConnectValidator, DBFConnectValidator

# Register your models here.

register = template.Library()

# ref https://stackoverflow.com/questions/45676500/django-admin-actions-on-single-object
class ImportTablesAdmin(admin.ModelAdmin):
    list_display = ('source_table', 'dest_table', 'uploadable', 'show_result', 'upload_record', 'run_import')
    list_filter = ('connects__name',)
    search_fields = ('source_table',)
    list_editable = ('uploadable',)
    save_on_top = True

    @admin.display(description=_('Import'))
    def run_import(self, obj):
        url = reverse('run-import-for-single-table', kwargs={'table_pk': obj.pk})
        return mark_safe(f'<a href="{url}" class="historylink">Run</a>')

    @admin.display(description=_('Task status'))
    def show_result(self, obj):
        status = _('unknown')
        if obj.message_id:
            result = Task.tasks.filter(pk=obj.message_id).get()
            if result:
                url = reverse('admin:django_dramatiq_task_change', args=[result.pk])
                return mark_safe(f'<a href="{url}" class="historylink">{result.status}</a>')
        return status


class ConnectSetAdmin(admin.ModelAdmin):
    list_display = ('source_conection', 'dest_conection', 'enabled', 'run_import')
    save_on_top = True

    def run_import(self, obj):
        connsets = self.model.consets.record(obj.pk)
        if connsets.enabled:
            url = reverse('run-import-for-database', kwargs={'poll_pk': obj.pk})
            link = mark_safe(f'<a href="{url}" class="historylink">Run</a>')
        else:
            link = mark_safe(f'<a href="#" class="historylink">Disable</a>')
        return link


class ConnectWrapperAdmin(admin.ModelAdmin):
    validate_form = None

    list_display = ('conname', 'engine', 'is_active')
    exclude = ['slug_name',]
    save_on_top = True

    form = ConnectWrapperForm

    # change_form_template = 'admin/core/custom_change_form.html'


    def save_form(self, request, form, change):
        if form.cleaned_data["engine"] == MSSQL_ENGINE:
            self.validate_form = SQLConnectValidator(request, form, change)
        else:
            self.validate_form = DBFConnectValidator(request, form, change)

        self.validate_form.validate()

        return super(ConnectWrapperAdmin, self).save_form(request, form, change)


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


    def delete_model(self, request, obj):
        self.validate_class.drop_database()
        super(ConnectWrapperAdmin, self).delete_model(request, obj)


admin.site.register(ImportTables, ImportTablesAdmin)
admin.site.register(ConnectSet, ConnectSetAdmin)
admin.site.register(ConnectWrapper, ConnectWrapperAdmin)


