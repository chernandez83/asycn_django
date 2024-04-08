import time
from celery import shared_task


@shared_task
def async_sleep(done):
    time.sleep(20)
    print(done)