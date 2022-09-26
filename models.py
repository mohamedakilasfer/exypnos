from sqlalchemy import Column, Integer, String, Float
from database import Base

class Women(Base):
    __tablename__ = 'Diabetes_Data'
    id = Column(Integer, primary_key=True, index=True)
    pregnancies = Column(Integer)
    glucose = Column(Integer)
    bp = Column(Integer)
    skinthickness = Column(Integer)
    insulin = Column(Integer)
    bmi = Column(Float)
    dpf = Column(Float)
    age = Column(Integer)