from datetime import timedelta

from celery.task import periodic_task

@periodic_task(run_every=timedelta(seconds=10))
def a():
    print('HELLO')
    return ' i running periodic task '