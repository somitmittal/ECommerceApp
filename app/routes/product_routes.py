from fastapi import APIRouter
from typing import List

from app.payloads.product import ProductCreate
from app.services.product_service import ProductService

router = APIRouter()


@router.get("/products", response_model=List[ProductCreate])
def get_products():
    return ProductService().get_products()


@router.post("/products")
def create_product(product_create: ProductCreate):
    return ProductService().create_product(product_create)
