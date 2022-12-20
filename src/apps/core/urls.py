from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from src.apps.common.dataclasses import ETL

from . import views

urlpatterns = [
    # path('admin/action/create-tables-action/<int:object_pk>',
    #      views.create_import_tables_action, name='import-tables-action'),
    # re_path(r'^admin/action/create-tables-list/(?P<object_pk>\d+)/$',
    #     views.create_or_update_import_tables_list, name='import-tables-action'),
    # re_path(r'^admin/action/' + f'{ETL.URLNAME.EXPORT_SINGLE_TABLE}' + '/(?P<table_pk>\d+)/$',
    #         views.run_import_for_single_table, name=f'{ETL.URLNAME.EXPORT_SINGLE_TABLE}'),
    path('admin/action/' + f'{ETL.URLNAME.EXPORT_SINGLE_TABLE}' + '/<int:table_pk>/<str:mode>/',
            views.run_import_for_single_table, name=f'{ETL.URLNAME.EXPORT_SINGLE_TABLE}'),
    # re_path(r'^admin/action/' + f'{ETL.URLNAME.PIPELINE_EXPORT_IMPORT}' + '/(?P<poll_pk>\d+)/$',
    #         views.run_import_for_database, name=f'{ETL.URLNAME.PIPELINE_EXPORT_IMPORT}'),
    path('admin/action/' + f'{ETL.URLNAME.PIPELINE_EXPORT_IMPORT}' + '/<int:poll_pk>/<str:mode>/',
            views.run_import_for_database, name=f'{ETL.URLNAME.PIPELINE_EXPORT_IMPORT}'),
    # path('admin/action/run-import-for-database/<int:table_pk>/<str:mode>/',
    #         views.run_import_for_database, name='run-import-for-database'),

    # path("sqlimport/", include("src.apps.sqlimport.urls")),

    # path('export/category/', views.CategoryExportView.as_view(), name='export-category'),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

if settings.MEDIA_ROOT:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)