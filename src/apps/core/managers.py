from django.db import models


class ImportTablesManager(models.Manager):
    def tables_for_import(self, connection_pull_pk):
        return self.filter(
            connects=connection_pull_pk,
            connects__enabled=True,
            uploadable=True).all()


class ConnectSetManager(models.Manager):
    def record(self, pk):
        return self.filter(pk=pk).get()

    def allowed_for_import(self):
        return self.filter(enabled=True).all()
