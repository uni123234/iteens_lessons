from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import DeclarativeBase


class Product(DeclarativeBase):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    stock = Column(Integer)

    supplies = relationship("Supply", back_populates="product")
    sales = relationship("Sale", back_populates="product")
