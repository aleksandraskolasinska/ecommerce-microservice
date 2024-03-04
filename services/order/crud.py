from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from fastapi import HTTPException
import requests

from ..common import models, schemas
from ..common.schemas import OrderCreate

SQLALCHEMY_DATABASE_URL = "postgresql://admin:admin@postgres:5432/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def create_order(db: Session, order: OrderCreate):
    r = requests.get(f"http://product:80/products/{order.product_id}")
    product = models.Product(**r.json())

    if product:
        price = product.price
        total = order.quantity * price

        db_order = models.Order(**order.dict(), price=price, total=total, product_name=product.name)
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        return db_order
    else:
        raise HTTPException(status_code=404, detail="Product not found")

def get_all_orders(db: Session):
    return db.query(models.Order).all()

def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()
