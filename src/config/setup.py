import os
import sys
import django
import django_dramatiq

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.config.settings')
django_dramatiq_dir = os.path.dirname(django_dramatiq.__file__)

if django_dramatiq_dir not in sys.path:
    sys.path.extend(django_dramatiq_dir)

django.setup()

# ################################################################################
# # UPDATE DATABASES dict from connects table !
# ################################################################################
from src.config import settings_manager
settings_manager.update_databases()
