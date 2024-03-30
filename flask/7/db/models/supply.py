from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from . import DeclarativeBase


class Supply(DeclarativeBase):
    __tablename__ = "supplies"

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)

    product_id = Column(Integer, ForeignKey("products.id"))
    product = relationship("Product", back_populates="supplies")
