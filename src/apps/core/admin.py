import json
from django import template
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_dramatiq.models import Task
from django.http import HttpResponseRedirect
from django.core.management import call_command
from django.db import connections
from django.contrib import messages
from django.contrib.admin.templatetags.admin_urls import add_preserved_filters

from src.config import settings
from .models import ConnectWrapper, ConnectSet, ImportTables
from .forms import ConnectWrapperForm


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
    CONNECTION_ID = None
    DATABASE_NAME = None
    _error_numbers = ('42000',)
    _error = False

    list_display = ('conname', 'engine', 'is_active')
    exclude = ['slug_name',]
    save_on_top = True

    form = ConnectWrapperForm

    # change_form_template = 'admin/core/custom_change_form.html'

    def save_form(self, request, form, change):
        self.CONNECTION_ID = ConnectWrapper.get_slug_name(conname=form.cleaned_data['conname']).lower()
        self.DATABASE_NAME = form.cleaned_data['name']

        if self._save_connection_params(form_cleaned_data=form.cleaned_data):
            self.create_database()
        return super(ConnectWrapperAdmin, self).save_form(request, form, change)

    def delete_model(self, request, obj):
        self.CONNECTION_ID = obj.conname.lower()
        self.DATABASE_NAME = obj.name
        try:
            self.drop_database()
            super(ConnectWrapperAdmin, self).delete_model(request, obj)
        except Exception as e:
            error_message = e.args[1]
            for error_number in self._error_numbers:
                if error_number in error_message:
                    messages.error(request, "%s" % error_message)
                    self._error = True
                else:
                    raise

    # def response_delete(self, request, obj_display, obj_id):
    #     if self._error:
    #         response_delete = super(ConnectWrapperAdmin, self).response_delete(request, obj_display, obj_id)
    #     #     post_url = reverse("admin:index", current_app=self.admin_site.name)
    #     #     return HttpResponseRedirect(post_url)
    #     else:
    #         response_delete = super(ConnectWrapperAdmin, self).response_delete(request, obj_display, obj_id)
    #     return response_delete


    def _save_connection_params(self, form_cleaned_data: dict):
        success = True
        try:
            connection_params= {}
            connection_params["ENGINE"] = form_cleaned_data['engine']
            connection_params["NAME"] = 'tempdb' # need database name for connection
            connection_params["USER"] = form_cleaned_data['user']
            connection_params["PASSWORD"] = form_cleaned_data['password']
            connection_params["HOST"] = form_cleaned_data['host']
            connection_params["PORT"] = form_cleaned_data['port']
            connection_params["OPTIONS"] = json.loads(form_cleaned_data['options'].replace("'", "\""))

            settings.DATABASES[self.CONNECTION_ID] = connection_params
        except ValueError as e:
            success = False
        return success

    def get_database_name(self):
        if self.DATABASE_NAME:
            return self.DATABASE_NAME
        else:
            raise ValueError(_("Database name is empty"))

    def _get_internal_db_connection(self):
        return connections[self.CONNECTION_ID]


    def _execute(self, sql):
        backend_databasewrapper = self._get_internal_db_connection()
        backend_databasewrapper.ensure_connection()
        cursor = backend_databasewrapper.create_cursor()
        cursor.execute(sql)
        # close connection
        backend_databasewrapper.close()


    def migrate_database(self):
        call_command('migrate', 'sqlimport', database=self.get_database_name(),
                     interactive=False, verbosity=0)


    def create_database(self):
        self._execute(
            'CREATE DATABASE "%s" ' % (self.get_database_name())
        )
        # Replace "tempdb" database name to real name
        settings.DATABASES[self.CONNECTION_ID]["NAME"] = self.DATABASE_NAME
        self.migrate_database()


    def drop_database(self):
        self._execute(
            'DROP DATABASE [%s]' % self.get_database_name()
        )


    def response_change(self, request, obj):
        opts = self.model._meta
        pk_value = obj._get_pk_val()
        preserved_filters = self.get_preserved_filters(request)

        if "_customaction" in request.POST:
            # handle the action on your obj
            redirect_url = reverse('admin:%s_%s_change' %
                                   (opts.app_label, opts.model_name),
                                   args=(pk_value,),
                                   current_app=self.admin_site.name)
            redirect_url = add_preserved_filters({'preserved_filters': preserved_filters, 'opts': opts}, redirect_url)
            return HttpResponseRedirect(redirect_url)

        else:
            return super(ConnectWrapperAdmin, self).response_change(request, obj)

admin.site.register(ImportTables, ImportTablesAdmin)
admin.site.register(ConnectSet, ConnectSetAdmin)
admin.site.register(ConnectWrapper, ConnectWrapperAdmin)


