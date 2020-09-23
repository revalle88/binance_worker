from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


@worker_init.connect
def configure():
    engine = create_engine('postgres://admin:123@localhost/binance', echo=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    Base = declarative_base()

    Base.metadata.create_all(engine)
