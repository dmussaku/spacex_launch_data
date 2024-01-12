import os
from celery import Celery

from config import CELERY_BACKEND, CELERY_BROKER
from main import main

os.environ.setdefault('CELERY_CONFIG_MODULE', 'config')
app = Celery('app', backend=CELERY_BACKEND, broker=CELERY_BROKER)
app.config_from_envvar('CELERY_CONFIG_MODULE')


@app.task
def poll_launches():
    main()
