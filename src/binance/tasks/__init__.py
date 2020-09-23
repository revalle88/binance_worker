from datetime import timedelta

from celery.task import periodic_task

from binance.celery_app import client


@periodic_task(run_every=timedelta(seconds=10))
def c():
    print('CCCCC')
    client.set('foo', 'bar')
    return ' i running periodic task '