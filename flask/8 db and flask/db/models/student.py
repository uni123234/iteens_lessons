from . import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey


class Student(Base):
    """
    Related with Group N-1
    """
    name: Mapped[str]
    second_name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"))
    group: Mapped["Group"] = relationship(
        back_populates="students"
    )

    def __repr__(self) -> str:
        return f"<{super().__repr__()}: {self.second_name} {self.name}>"
