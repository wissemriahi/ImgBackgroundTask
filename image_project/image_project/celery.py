
import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'image_project.settings')
celery_app = Celery("image_project")
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()
