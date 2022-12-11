from typing import List

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from .functions import table_import_info
from .functions import tables_import_info_list
from .tasks import process_database_import
from src.apps.common.dataclasses import ImportInfo

# Create your views here.

"""
https://stackoverflow.com/questions/45676500/django-admin-actions-on-single-object
Reversing admin URLs¶
When an AdminSite is deployed, the views provided by that site are accessible using Django’s URL
reversing system.

The AdminSite provides the following named URL patterns:

Page	URL name	Parameters
Index	index
Login	login
Logout	logout
Password change	password_change
Password change done	password_change_done
i18n JavaScript	jsi18n
Application index page	app_list	app_label
Redirect to object’s page	view_on_site	content_type_id, object_id
Each ModelAdmin instance provides an additional set of named URLs:

Page	URL name	Parameters
Changelist	{{ app_label }}_{{ model_name }}_changelist
Add	{{ app_label }}_{{ model_name }}_add
History	{{ app_label }}_{{ model_name }}_history	object_id
Delete	{{ app_label }}_{{ model_name }}_delete	object_id
Change	{{ app_label }}_{{ model_name }}_change	object_id
"""
def run_import_for_single_table(
    request: object, table_pk: int, mode: str
) -> HttpResponseRedirect:
    """
    Run dramatiq task importing data from single DBF table

    :param request:
    :param table_pk:
    :param mode:
    :return:
    """

    t_list: List[ImportInfo] = table_import_info(table_pk)

    if len(t_list) > 0:
        process_database_import(t_list)

    messages.success(
        request,
        f"Process import data from table {t_list[0].source_table_name} to {t_list[0].dest_table_name} has started...",
    )
    return HttpResponseRedirect(reverse("admin:core_importtables_changelist"))


def run_import_for_database(
    request: object, poll_pk: int, mode: str
) -> HttpResponseRedirect:
    """
    Run process importing data from any source to MSSQL database

    :param request:
    :param poll_pk:
    :return HttpResponseRedirect:
    """
    from .models import ConnectSet

    t_list: List[ImportInfo] = tables_import_info_list(poll_pk)
    poll_name: str = ConnectSet.consets.record(pk=poll_pk).name

    if len(t_list) > 0:
        # pipeline_steps_for_import(t_list, mode=mode)
        # process_database_import(t_list, mode=mode)
        process_database_import(t_list)
        messages.info(
            request, f"Process import data from {poll_name} is running!"
        )
    else:
        messages.warning(
            request, f"No needs import data from {poll_name} it's up to date!"
        )

    return HttpResponseRedirect(reverse("admin:core_connectset_changelist"))
