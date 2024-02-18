import os
from celery import Celery
from celery.signals import worker_ready

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
app = Celery("server")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
