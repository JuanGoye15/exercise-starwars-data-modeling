import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    user_age = Column(Integer, ForeignKey('user.age'))
    email = Column(String(250), nullable=False)    
    # favorites = relationship("favorites")

class Planets(Base):
    __tablename__ = 'Planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    diameter = Column(Integer)
    gravity = Column(Integer)
    


class Characters(Base):
    __tablename__ = 'Characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(Integer)
    height = Column(Integer)
    gender = Column(String(250), nullable=False)

class Species(Base):
    __tablename__ = 'Species'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    classification = Column(String(250), nullable=False)
    average_height = Column(Integer)
    language = Column(String(250), nullable=False)
    average_lifespan = Column(Integer)

class Favorites(Base):
    __tablename__ = 'Favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    id_users = Column(Integer, ForeignKey('user.id  '))
    id_planets = Column(String(250))
    id_characters = Column(String(250), nullable=False)
    # id = relationship("id")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
