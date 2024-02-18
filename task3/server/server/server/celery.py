import os
from celery import Celery
from celery.signals import worker_ready

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
app = Celery("server")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@worker_ready.connect
def at_start(sender, **k):
    with sender.app.connection() as conn:
        sender.app.send_task('apps.core.tasks.load_data_from_source_1', connection=conn)
        sender.app.send_task('apps.core.tasks.load_data_from_source_2', connection=conn, countdown=20)

