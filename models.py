from sqlalchemy import Column,Integer,String,Float
from app.database import Base

class Bill(Base):
    __tablename__='bills'
    id=Column(Integer,primary_key=True)
    units=Column(Integer)
    amount=Column(Float)
