from fastapi import APIRouter

from app.payloads.order import OrderCreate
from app.services.order_service import OrderService

router = APIRouter()


@router.post("/orders")
def create_order(order_create: OrderCreate):
    return OrderService().create_order(order_create)
