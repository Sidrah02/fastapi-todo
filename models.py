from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# Create Base class for all models
Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
