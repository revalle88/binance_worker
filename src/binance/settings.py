import os

book_order_url = os.getenv("BOOK_ORDER_URI")
history_url = os.getenv("HISTORY_URI")
redis_dsn = os.getenv("REDIS_DSN")
binance_symbol=os.getenv("BINANCE_SYMBOL")
binance_limit=os.getenv("BINANCE_LIMIT")
binance_interval=os.getenv("BINANCE_INTERVAL")