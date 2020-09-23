from celery import Celery

app = Celery('', backend='amqp',
             broker='rabbitmq')

app.autodiscover_tasks(['binance.tasks'])



