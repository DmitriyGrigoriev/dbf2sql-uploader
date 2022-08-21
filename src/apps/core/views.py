from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import ConnectSet, ImportTables



from src.apps.core.tasks import (
    process_database_import, process_import,
    print_error, update_last_write_if_success_result,
)

# Create your views here.
# https://stackoverflow.com/questions/45676500/django-admin-actions-on-single-object
# Reversing admin URLs¶
# When an AdminSite is deployed, the views provided by that site are accessible using Django’s URL
# reversing system.
#
# The AdminSite provides the following named URL patterns:
#
# Page	URL name	Parameters
# Index	index
# Login	login
# Logout	logout
# Password change	password_change
# Password change done	password_change_done
# i18n JavaScript	jsi18n
# Application index page	app_list	app_label
# Redirect to object’s page	view_on_site	content_type_id, object_id
# Each ModelAdmin instance provides an additional set of named URLs:
#
# Page	URL name	Parameters
# Changelist	{{ app_label }}_{{ model_name }}_changelist
# Add	{{ app_label }}_{{ model_name }}_add
# History	{{ app_label }}_{{ model_name }}_history	object_id
# Delete	{{ app_label }}_{{ model_name }}_delete	object_id
# Change	{{ app_label }}_{{ model_name }}_change	object_id



def run_import_for_single_table(request, table_pk):
    """Run dramatiq task importing data from single DBF table"""
    kwargs = ImportTables.tables.get_kwargs(table_pk=table_pk)
    process_import.send_with_options(
        kwargs = kwargs,
        # args=(object_pk, source_connection_name, source_table, dest_connection_name, dest_table),
        on_failure=print_error,
        on_success=update_last_write_if_success_result,
    )

    messages.success(request, f"Process import data from table {kwargs['source_table_name']} to {kwargs['dest_table_name']} has started...")
    return HttpResponseRedirect(
       reverse('admin:core_importtables_changelist')
    )


def run_import_for_database(request, poll_pk)-> HttpResponseRedirect:
    t_list = ImportTables.tables.tables_import_list(poll_pk)
    poll_name = ConnectSet.consets.record(pk=poll_pk).name

    if len(t_list)>0:
        process_database_import(t_list)
        messages.info(request, f'Process import data from {poll_name} is running!')
    else:
        messages.info(request, f'No needs import data from {poll_name} it\'s up to date!')

    return HttpResponseRedirect(
       reverse('admin:core_connectset_changelist')
    )
