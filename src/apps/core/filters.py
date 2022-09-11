from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from src.apps.core.models import DBF_ENGINE, MSSQL_ENGINE

class PipelineListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('pipeline')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'pipeline'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('all', _('All')),
            ('enable', _('Enabled')),
            ('disable', _('Disabled')),
        )

    def choices(self, changelist):
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == lookup,
                'query_string': changelist.get_query_string({
                    self.parameter_name: lookup,
                }, []),
                'display': title,
            }

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == 'enable':
            return queryset.filter(enabled=True)
        if self.value() == 'disable':
            return queryset.filter(enabled=False)
        if self.value() == None:
            return queryset.filter(enabled=True)

class ConnectTypeListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('export/import type')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'export-type'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            (DBF_ENGINE, _('Export from DBF')),
            (MSSQL_ENGINE, _('Import to Doc2sql')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == DBF_ENGINE:
            return queryset.filter(engine=DBF_ENGINE)
        if self.value() == MSSQL_ENGINE:
            return queryset.filter(engine=MSSQL_ENGINE)