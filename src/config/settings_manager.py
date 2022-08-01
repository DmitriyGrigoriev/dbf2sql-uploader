import json
from src.config import settings
from src.apps.core.models import ConnectWrapper

def update_databases():
    """Refresh database settings from connects table settings"""

    databases = ConnectWrapper.objects.filter(is_active=True).all()
    for database in databases:
        new_database = {}
        new_database["ENGINE"] = database.engine
        new_database["NAME"] = database.name
        new_database["USER"] = database.user
        new_database["PASSWORD"] = database.password
        new_database["HOST"] = database.host
        new_database["PORT"] = database.port
        new_database["OPTIONS"] = json.loads(database.options.replace("'", "\""))
        ####### Update settings.DATABASES dict ########
        settings.DATABASES[database.slug_name] = new_database


# from mssql.base import DatabaseWrapper
