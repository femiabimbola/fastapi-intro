# models.py
from sqlalchemy import Column, Integer, String, Float, Text
from db import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False, default=0)

    def __repr__(self):
        return f"<Product {self.name} (Qty: {self.quantity})>"