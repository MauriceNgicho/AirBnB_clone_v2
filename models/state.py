#!/usr/bin/python3
"""A State module for the HBNB project"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """State class that contains name and links cities and states"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    # Establish a relationship of one-to-many between State and City
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')

    @property
    def cities(self):
        """Returns a list of City instances linked to the State"""
        if getenv('HBNB_TYPE_STORAGE') != 'db':
            return [
                city for city in models.storage.all(City).values()
                if city.state_id == self.id
            ]
        return []
