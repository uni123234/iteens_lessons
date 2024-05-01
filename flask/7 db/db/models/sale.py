from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from . import DeclarativeBase


class Sale(DeclarativeBase):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)

    product_id = Column(Integer, ForeignKey("products.id"))
    product = relationship("Product", back_populates="sales")

    customer_id = Column(Integer, ForeignKey("customers.id"))
    customer = relationship("Customer", back_populates="sales")
