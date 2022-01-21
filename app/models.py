from sqlalchemy import Column, Float, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Wells(Base):
    __tablename__ = 'wells'

    id_ = Column(String, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    depth = Column(Float)
    gradient = Column(Float)
