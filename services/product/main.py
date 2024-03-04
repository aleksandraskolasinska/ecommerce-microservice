from typing import Union, List

from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import HTMLResponse

from pydantic import BaseModel, Field, HttpUrl
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

from ..common import models, schemas
from ..common.database import SessionLocal, engine

from .crud import create_product, get_all_products, get_product, delete_product  # Add this line


from starlette.requests import Request
 
import os

# Create DB Tables
models.Base.metadata.create_all(bind=engine)


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create product endpoint
@app.post('/products/create', response_model=schemas.Product)
def create_product_endpoint(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return create_product(db=db, product_data=product.dict())

# Get all products endpoint
@app.get('/products', response_model=List[schemas.Product])
def get_all_products_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_all_products(db=db, skip=skip, limit=limit)

# Get a single product endpoint
@app.get('/products/{product_id}', response_model=schemas.Product)
def get_product_endpoint(product_id: int, db: Session = Depends(get_db)):
    return get_product(db=db, product_id=product_id)

# Delete a product endpoint
@app.delete('/products/del/{product_id}', response_model=schemas.DeleteResponse)
def delete_product_endpoint(product_id: int, db: Session = Depends(get_db)):
    return delete_product(db=db, product_id=product_id)


