from celery import Celery

from binance.configure import configure
#
# configure()

app = Celery('tasks', backend='amqp',
             broker='rabbitmq')

