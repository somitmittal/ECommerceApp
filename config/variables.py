from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./ecommerce.db"