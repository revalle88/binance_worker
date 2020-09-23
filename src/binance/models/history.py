from sqlalchemy import Column, Integer, String
from binance.configure import Base


class History(Base):
    __tablename__ = 'history'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f'Name {self.name}'
