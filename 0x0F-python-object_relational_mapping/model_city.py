#!/usr/bin/python3
"""
Module defines the city class
"""
import sys
from sqlalchemy import Column, Integer, String
from model_state import Base


class City(Base):
    """City class for a MySQL database"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
