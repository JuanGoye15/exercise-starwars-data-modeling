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
    id = Column(Integer, ForeignKey('users.id'))
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    user_age = Column(Integer, ForeignKey('user.age'))
    email = Column(String(250), nullable=False)    
    id = relationship("Favorites")

class Planets(Base):
    __tablename__ = 'Planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, ForeignKey('planets.id'))
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    diameter = Column(Integer)
    gravity = Column(Integer)
    id = relationship("Favorites")
    


class Characters(Base):
    __tablename__ = 'Characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, ForeignKey('users.id'))
    name = Column(String(250), nullable=False)
    birth_year = Column(Integer)
    height = Column(Integer)
    gender = Column(String(250), nullable=False)
    id = relationship("Favorites")

class Species(Base):
    __tablename__ = 'Species'
    id = Column(Integer, ForeignKey('species.id'))
    name = Column(String(250), nullable=False)
    classification = Column(String(250), nullable=False)
    average_height = Column(Integer)
    language = Column(String(250), nullable=False)
    average_lifespan = Column(Integer)
    id = relationship("Favorites")

class Favorites(Base):
    __tablename__ = 'Favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    id_users = Column(Integer, ForeignKey('users.id'))
    id_planets = Column(Integer, ForeignKey('planets.id'))
    id_characters = Column(Integer, ForeignKey('characters.id'))
    id = relationship("Favorites")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
