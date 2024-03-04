from pydantic import BaseModel, create_model, ValidationError, validate_arguments, ValidationError

from typing import List


class ProductBase(BaseModel):
    name: str
    price: float
    quantity: int
    

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True

class DeleteResponse(BaseModel):
    message: str


class OrderBase(BaseModel):
    product_id: int
    quantity: int

class OrderCreate(OrderBase):
    product_id: int
    quantity: int

class Order(OrderBase):
    id: int
    product_name: str
    price: float
    total: float

    class Config:
        orm_mode = True