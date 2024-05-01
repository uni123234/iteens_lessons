from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import DeclarativeBase


class Customer(DeclarativeBase):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    sales = relationship("Sale", back_populates="customer")
