import requests
from binance_worker.settings import book_order_url


class BookService:
    @classmethod
    def get_book(cls, limit=5000, symbol='BTCUSDT'):
        print('inside')
        print(book_order_url)
        resp = requests.get(f'{book_order_url}?symbol={symbol}&limit={limit}')
        print(resp)