import json

import requests
import pymongo
from binance.settings import book_order_url, history_url, mongo_dsn


import logging
logger = logging.getLogger(__name__)


class BookService:
    client = pymongo.MongoClient(mongo_dsn)
    db = client['binance']
    history_table = db['history']

    @classmethod
    def get_book(cls, limit=5000, symbol='BTCUSDT'):
        return json.loads(
            requests.get(
                f'{book_order_url}?symbol={symbol}&limit={limit}'
            ).text
        )

    @classmethod
    def get_history(cls, symbol='BTCUSDT', interval='5m', limit='1'):
        return json.loads(
            requests.get(
                f'{history_url}?symbol={symbol}&interval={interval}&limit={str(limit)}'
            ).text
        )

    @classmethod
    def save_book(cls, book):
        try:
            cls.history_table.save(book)
        except Exception as e:
            logger.error('Mongo save error!!!')
            logger.error(e)
        return ' success '
