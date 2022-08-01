from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # path('admin/action/create-tables-action/<int:object_pk>',
    #      views.create_import_tables_action, name='import-tables-action'),
    re_path(r'^admin/action/create-tables-list/(?P<object_pk>\d+)/$',
        views.create_or_update_import_tables_list, name='import-tables-action'),
    re_path(r'^admin/action/run-import-for-single-table/(?P<table_pk>\d+)/$',
            views.run_import_for_single_table, name='run-import-for-single-table'),
    re_path(r'^admin/action/run-import-for-database/(?P<poll_pk>\d+)/$',
            views.run_import_for_database, name='run-import-for-database'),

    # path("sqlimport/", include("src.apps.sqlimport.urls")),

    # path('export/category/', views.CategoryExportView.as_view(), name='export-category'),

]

if settings.MEDIA_ROOT:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)