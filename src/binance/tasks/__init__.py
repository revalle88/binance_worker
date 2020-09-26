import json

from celery.task import periodic_task
from binance.services.book import BookService
from datetime import timedelta
from binance.settings import (
    binance_symbol, binance_limit, binance_interval, history_interval,
    history_limit
)


@periodic_task(run_every=timedelta(seconds=int(binance_interval)))
def save_data():
    book = BookService.get_book(limit=binance_limit, symbol=binance_symbol)
    history = BookService.get_history(
        symbol=binance_symbol, interval=history_interval, limit=history_limit
    )
    book['history'] = history
    return BookService.save_book(json.dumps(book))
