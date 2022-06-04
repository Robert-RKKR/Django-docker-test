# Python Import:
import time

# Celery Import:
from celery import shared_task
from autocli.celery import app
from asgiref.sync import async_to_sync


@shared_task(bind=True, track_started=True, name='Log collector')
def test_task(self):

    time.sleep(2)
    print('RKKR')

    return 'RKKR'
