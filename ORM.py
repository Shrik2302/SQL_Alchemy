from sqlalchemy import Table, Column, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

DB_URL = 'postgresql+psycopg2://postgres:root@localhost/basic'
engine = create_engine(DB_URL)

Base = declarative_base()

class Cookie(Base):
    __tablename__ = 'cookies'

    cookie_id = Column(Integer(), primary_key = True)
    cookie_name = Column(String(50), index=True)
    cookie_recipe_url = Column(String(255))
    cookie_sku = Column(String(50))
    quantity = Column(Integer())
    unit_cost = Column(Numeric(12,2))


Base.metadata.create_all(engine)

print(Cookie.__table__)
print("table created")