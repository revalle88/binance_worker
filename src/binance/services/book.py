import requests
import redis
from binance.settings import book_order_url
from binance.settings import redis_dsn
import time

import logging
logger = logging.getLogger(__name__)


class BookService:
    client = redis.Redis.from_url(redis_dsn)

    @classmethod
    def get_book(cls, limit=5000, symbol='BTCUSDT'):
        resp = requests.get(f'{book_order_url}?symbol={symbol}&limit={limit}')
        return resp

    @classmethod
    def save_book(cls, book):
        try:
            cls.client.set(str(int(time.time())) , book)
        except Exception as e:
            logger.error('Redis save error!!!')
            logger.error(e)
        return ' success '