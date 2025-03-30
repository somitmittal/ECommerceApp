from typing import Any, Dict

from fastapi import HTTPException

from app.db import DatabaseInterface, SQLiteDB
from app.singleton import singleton
from app.models.order import Order
from app.models.product import Product
from app.payloads.order import OrderCreate


@singleton
class OrderService:
    def __init__(self, db_interface: DatabaseInterface = SQLiteDB()):
        self.db = db_interface.connect()

    def create_order(self, order: OrderCreate) -> Dict[str, Any]:
        total_price = 0
        for item in order.products:
            product = (
                self.db.query(Product).filter(Product.id == item.product_id).first()
            )
            if not product:
                raise HTTPException(
                    status_code=404,
                    detail=f"Product with Id: {item.product_id} does not exist",
                )
            if product.stock < item.quantity:
                raise HTTPException(
                    status_code=400,
                    detail=f"Insufficient stock for product {item.product_id}",
                )
            total_price += product.price * item.quantity
            product.stock -= item.quantity
        db_order = Order(total_price=total_price, status="completed")
        self.db.add(db_order)
        self.db.commit()
        return {"message": "Order placed successfully", "total_price": total_price}
