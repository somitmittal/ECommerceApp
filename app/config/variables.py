# Database setup
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./ecommerce.db"
ENGINE = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
DB = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)()
Base = declarative_base()
