#!/usr/bin/python3
""" A State module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class State(BaseModel, Base):
    """ State class that contains name and links city and states class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    # Establis a relationship of one to many between State and City.
    cities = relationship('City', backref='state', cascade='all, delete-orphan')

