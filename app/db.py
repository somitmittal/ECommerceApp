from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from config.variables import SQLALCHEMY_DATABASE_URL
from app.singleton import singleton

from abc import ABC, abstractmethod


class DatabaseInterface(ABC):
    @abstractmethod
    def connect(self):
        """Establish a database connection."""
        pass

    @abstractmethod
    def disconnect(self):
        """Close the database connection."""
        pass


@singleton
class SQLiteDB(DatabaseInterface):
    def __init__(self):
        self.engine = create_engine(
            SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
        )
        self.db = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)()
        self.base = declarative_base()
        self.base.metadata.create_all(bind=self.engine)

    def connect(self):
        yield self.db

    def disconnect(self):
        self.db.close()
