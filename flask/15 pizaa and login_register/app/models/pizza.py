from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Pizza(Base):
    __tablename__ = "pizza"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(256))
    price: Mapped[float] = mapped_column(Integer)

    def __repr__(self):
        return f"Pizza: {self.name}"
