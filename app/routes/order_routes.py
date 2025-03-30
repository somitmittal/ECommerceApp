from fastapi import APIRouter

from payloads.order import OrderCreate
from services.order_service import OrderService

router = APIRouter()


@router.post("/orders")
def create_order(order_create: OrderCreate):
    return OrderService().create_order(order_create)
