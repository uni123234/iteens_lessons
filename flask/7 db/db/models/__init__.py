from .customer import Customer
from .sale import Sale
from .supply import Supply
from .product import Product
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///my_db.sql", echo=True)
Session = sessionmaker(bind=engine)
DeclarativeBase = declarative_base()
