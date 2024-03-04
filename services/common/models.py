from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from .database import Base



class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, index=True)
    price = Column(Float)
    quantity = Column(Integer)
    total = Column(Float)
    product_name = Column(String)
    status = Column(String)