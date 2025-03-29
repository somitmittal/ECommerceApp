from app.db import DatabaseInterface, SQLiteDB
from app.singleton import singleton
from models.product import Product
from payloads.product import ProductCreate


@singleton
class ProductService:
    def __init__(self, db_interface: DatabaseInterface = SQLiteDB()):
        self.db = db_interface.connect()

    def get_products(self):
        self.db.query(Product).all()

    def create_product(self, product_create: ProductCreate) -> Product :
        db_product = Product(**product_create.model_dump())
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product
