# src/models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    price = Column(String)
    availability = Column(String)
    category = Column(String)
    rating = Column(String)
    product_url = Column(String)
