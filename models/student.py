from sqlalchemy import Column, Integer, String, Float
from database.connection import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    age = Column(Integer, nullable=False)
    course = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    marks = Column(Float, nullable=False)