from django.contrib import admin

from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
# from import_export.resources import ModelResource
# from import_export.instance_loaders import CachedInstanceLoader
# from .models import DataSourceInfo, TDclHead

# Register your models here.
# @admin.register(DataSourceInfo)
# class DataSourceInfoAdmin(admin.ModelAdmin):
#     pass
#
# class DclheadAdmin(ImportMixin, admin.ModelAdmin):
#     pass

# class DclheadResource(ModelResource):
#     # g07x = models.CharField(max_length=23, blank=True, null=True)
#
#     class Meta:
#         model = TDclHead
#         use_bulk = True
#         batch_size = 1000
#         skip_unchanged = True
#         #skip_diff = True
#         # This flag can speed up imports
#         # Cannot be used when performing updates
#         # force_init_instance = True
#         # This instance loader work only when there is one ``import_id_fields``
#         instance_loader_class = CachedInstanceLoader
#
#     def before_import_row(self, row, row_number=None, **kwargs):
#         if 'g071' in row and 'g072' in row and 'g073' in row:
#             year, day, mounth = row['g072'].split('-')
#             g072 = f"{row['g071']}/{day + mounth + year[2:]}/{row['g073']}"
#         pass


# admin.site.register(TDclHead, DclheadAdmin)
# admin.site.register(DataSourceInfo, DataSourceInfoAdmin)