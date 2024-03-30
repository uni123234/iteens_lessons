from . import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List


class Group(Base):
    """
    Related with Student 1-N
    """
    name: Mapped[str]

    students: Mapped[List["Student"]] = relationship(
        back_populates="group", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<{super().__repr__()}: {self.name}>"
