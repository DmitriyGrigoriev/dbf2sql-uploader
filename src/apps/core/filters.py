from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django_dramatiq.models import Task

from src.apps.core.models import DBF_ENGINE
from src.apps.core.models import MSSQL_ENGINE


class PipelineStatusListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _("status")

    # Parameter for the filter that will be used in the URL query.
    parameter_name = "pipeline-status"

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ("enqueued", _("Enqueued")),
            ("delayed", _("Delayed")),
            ("running", _("Running")),
            ("failed", _("Failed")),
            ("done", _("Done")),
            ("skipped", _("Skipped")),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value():
            return queryset.filter(
                message_id__in=Task.tasks.filter(status=self.value())
            )
        else:
            return queryset.filter(connects__enabled=True)


class PipelineTablesListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _("pipeline owner")

    # Parameter for the filter that will be used in the URL query.
    parameter_name = "pipeline-tables"

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return [
            c
            for c in model_admin.model.tables.values_list(
                "connects_id", "connects__name"
            )
            .filter(connects__enabled=True)
            .distinct()
        ]

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value():
            return queryset.filter(connects__id__exact=self.value())
        else:
            return queryset.filter(connects__enabled=True)


class PipelineListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _("pipelines")

    # Parameter for the filter that will be used in the URL query.
    parameter_name = "pipeline"

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ("all", _("All")),
            ("enable", _("Enabled")),
            ("disable", _("Disabled")),
        )

    def choices(self, changelist):
        for lookup, title in self.lookup_choices:
            yield {
                "selected": self.value() == lookup,
                "query_string": changelist.get_query_string(
                    {
                        self.parameter_name: lookup,
                    },
                    [],
                ),
                "display": title,
            }

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == "enable":
            return queryset.filter(enabled=True)
        if self.value() == "disable":
            return queryset.filter(enabled=False)
        if self.value() == None:
            return queryset.filter(enabled=True)


class ConnectTypeListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _("export/import engine")

    # Parameter for the filter that will be used in the URL query.
    parameter_name = "export-type"

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            (DBF_ENGINE, _("DBF source")),
            (MSSQL_ENGINE, _("MSSQL source")),
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
