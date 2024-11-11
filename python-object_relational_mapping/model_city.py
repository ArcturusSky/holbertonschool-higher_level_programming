#!/usr/bin/python3
"""
Contains the class definition of a City
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class City(Base):
    """City class"""
    __tablename__ = 'cities'
    # Your class definition here
    pass
