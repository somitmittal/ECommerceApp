from sqlalchemy import Column, Integer, String, Float

from config.variables import Base


class Product(Base):
    __tablename__: str = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    stock = Column(Integer)
