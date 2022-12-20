import re
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
# from django.views.static import serve as mediaserve
from src.apps.common.dataclasses import ETL


from . import views

urlpatterns = [
    path('admin/action/' + f'{ETL.URLNAME.EXPORT_SINGLE_TABLE}' + '/<int:table_pk>/<str:mode>/',
            views.run_import_for_single_table, name=f'{ETL.URLNAME.EXPORT_SINGLE_TABLE}'),
    # re_path(r'^admin/action/' + f'{ETL.URLNAME.PIPELINE_EXPORT_IMPORT}' + '/(?P<poll_pk>\d+)/$',
    #         views.run_import_for_database, name=f'{ETL.URLNAME.PIPELINE_EXPORT_IMPORT}'),
    path('admin/action/' + f'{ETL.URLNAME.PIPELINE_EXPORT_IMPORT}' + '/<int:poll_pk>/<str:mode>/',
            views.run_import_for_database, name=f'{ETL.URLNAME.PIPELINE_EXPORT_IMPORT}'),
    # path('admin/action/run-import-for-database/<int:table_pk>/<str:mode>/',
    #         views.run_import_for_database, name='run-import-for-database'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# else:
#     urlpatterns += [
#         re_path(
#             r"^%s(?P<path>.*)$" % re.escape(settings.STATIC_URL.lstrip("/")),
#             mediaserve, {'document_root': settings.STATIC_ROOT}
#         ),
#     ]
    # thing = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # print(thing, type(thing[0]))
    # print(thing[0].pattern)
    # print(dir(thing[0]))
    # print(urlpatterns[1], type(urlpatterns[1]))

    # urlpatterns += [
    #     re_path(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',
    #             mediaserve, {'document_root': settings.MEDIA_ROOT}
    #     ),
    #     re_path(f'^{settings.STATIC_URL.lstrip("/")}(?P<path>.*)$',
    #             mediaserve, {'document_root': settings.STATIC_ROOT}
    #             ),
    # ]