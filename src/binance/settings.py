import os

book_order_url = os.getenv("BOOK_ORDER_URI")
history_url = os.getenv("HISTORY_URI")
history_interval = os.getenv("HISTORY_INTERVAL")
history_limit = str(os.getenv("HISTORY_LIMIT"))
mongo_dsn = os.getenv("MONGO_DSN")
binance_symbol=os.getenv("BINANCE_SYMBOL")
binance_limit=os.getenv("BINANCE_LIMIT")
binance_interval=os.getenv("BINANCE_INTERVAL")