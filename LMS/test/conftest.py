import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lms.settings')

<<<<<<< HEAD

def pytest_configure():
    settings.DEBUG = False
    django.setup()
=======
def pytest_configure():
    settings.DEBUG = False
    django.setup()
>>>>>>> d8879cae0a1a0ba6382c6c756a94bf5d405530fc
