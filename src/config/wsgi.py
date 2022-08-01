import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.config.settings')

application = get_wsgi_application()

################################################################################
# UPDATE DATABASES dict from connects table !
################################################################################
from src.config import settings_manager
settings_manager.update_databases()
