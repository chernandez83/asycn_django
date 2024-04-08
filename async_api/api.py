import time

from .tasks import async_sleep

def api_slow():
    async_sleep.delay('tarea terminada')
    print('tarea enviada')