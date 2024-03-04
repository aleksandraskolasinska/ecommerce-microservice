from sqlalchemy.orm import Session

from ..common import models, schemas


def create_product(db: Session, product_data: dict):
    db_product = models.Product(**product_data)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_all_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def delete_product(db: Session, product_id: int):
    db.query(models.Product).filter(models.Product.id == product_id).delete()
    db.commit()
    return schemas.DeleteResponse(message="Product deleted successfully")