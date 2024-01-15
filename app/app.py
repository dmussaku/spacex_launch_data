import os
from celery import Celery
from celery.schedules import crontab

from config import CELERY_BACKEND, CELERY_BROKER
from main import main

os.environ.setdefault('CELERY_CONFIG_MODULE', 'config')
app = Celery('app', backend=CELERY_BACKEND, broker=CELERY_BROKER)
app.config_from_envvar('CELERY_CONFIG_MODULE')
app.conf.beat_schedule = {
 "run-me-every-ten-seconds": {
    "task": "app.poll_launches",
    "schedule": crontab(minute="*/5")
 }
}


@app.task
def poll_launches():
    main()
