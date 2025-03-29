from typing import Any, Dict

from fastapi import HTTPException

from app.db import DatabaseInterface, SQLiteDB
from app.singleton import singleton
from models.order import Order
from models.product import Product
from payloads.order import OrderCreate


@singleton
class OrderService:
    def __init__(self, db_interface: DatabaseInterface = SQLiteDB()):
        self.db = db_interface.connect()

    def create_order(self, order: OrderCreate) -> Dict[str, Any]:
        total_price = 0
        for item in order.products:
            product = self.db.query(Product).filter(Product.id == item.product_id).first()
            if not product or product.stock < item.quantity:
                raise HTTPException(status_code=400, detail=f"Insufficient stock for product.py {item.product_id}")
            total_price += product.price * item.quantity
            product.stock -= item.quantity
        db_order = Order(total_price=total_price, status="completed")
        self.db.add(db_order)
        self.db.commit()
        return {"message": "Order placed successfully", "total_price": total_price}