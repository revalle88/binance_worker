from celery import Celery
from celery.task import periodic_task
from binance.services.book import BookService
from datetime import timedelta
from binance.settings import binance_symbol, binance_limit, binance_interval

app = Celery('', backend='amqp',
             broker='rabbitmq')


@periodic_task(run_every=timedelta(seconds=int(binance_interval)))
def save_stakan_data():
    book = BookService.get_book(limit=binance_limit, symbol=binance_symbol).content
    return BookService.save_book(book)


