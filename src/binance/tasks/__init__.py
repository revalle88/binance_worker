import time

from celery.task import periodic_task
from binance.services.book import BookService
from datetime import timedelta
from binance.settings import (
    binance_symbol, binance_limit, binance_interval, history_interval,
    history_limit
)


@periodic_task(run_every=timedelta(seconds=int(binance_interval)))
def save_data():
    send_time = str(int(time.time()))
    book = BookService.get_book(limit=binance_limit, symbol=binance_symbol)
    history = BookService.get_history(
        symbol=binance_symbol, interval=history_interval, limit=history_limit
    )
    book['history'] = history
    book['send_time'] = send_time
    book['_id'] = send_time
    return BookService.save_book(book)
