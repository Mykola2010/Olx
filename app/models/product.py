from __future__ import annotations

from sqlalchemy import (
    String
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)
from app.models.base import Base


class Product(Base):
    __tablename__ = "product"
    __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(240), nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    image: Mapped[str] = mapped_column(String(240), nullable=True)

    def __str__(self):
        return self.name.capitalize()

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price})>"
