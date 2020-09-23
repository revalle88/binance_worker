from binance_worker.services.book import BookService
import pytest_mock


def test_book_order(monkeypatch):
    # monkeypatch.setenv('BOOK_ORDER_URI', 'https://api.binance.com/api/v3/depth')
    # book_order_url = mocker.patch('binance_worker.settings.book_order_url')
    # book_order_url = 'https://api.binance.com/api/v3/depth'
    resp = BookService.get_book()
    print(resp)
    assert False
