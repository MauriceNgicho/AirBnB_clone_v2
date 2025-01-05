#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, ForeignKey, PrimaryKeyConstraint, String
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = cities
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), nullable=False, ForeignKey(state_id))
