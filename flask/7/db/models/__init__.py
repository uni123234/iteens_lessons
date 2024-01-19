from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///my_db.sql", echo=True)
Session = sessionmaker(bind=engine)
DeclarativeBase = declarative_base()

from .product import Product
from .supply import Supply
from .sale import Sale
from .customer import Customer
