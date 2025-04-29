from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.db import Base

class Vehicle(Base):
    __tablename__ = "vehicles"

    id:    Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    plate: Mapped[str] = mapped_column(String(10), unique=True, index=True)
    brand: Mapped[str] = mapped_column(String(50))
    model: Mapped[str] = mapped_column(String(50))
    year:  Mapped[int] = mapped_column(Integer)
    color: Mapped[str] = mapped_column(String(50))          # NOT NULL
