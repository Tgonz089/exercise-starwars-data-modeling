import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String(256), unique=True, nullable = False)
    name = Column(String(256))
    password = Column (String(256), nullable = False)

class Person(Base):
    __tablename__ = 'Person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    person_fav_id = Column(Integer)
    name = Column(String(256))
    eye_color = Column(String(25))
    hair_color = Column(String(25))
    gender = Column(String(25))
    height = Column(Float)
    mass = Column(Float)
    Planet_id = Column(Integer, ForeignKey("Planet.id"))
    person = relationship("Person_To_Favorites")

class Planet(Base):
    __tablename__ = 'Planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_fav_id = Column(Integer)
    planet_name = Column(String(256))
    population = Column(String(256))
    terrain = Column(String(25))
    gravity = Column(Integer)
    orbital_period = Column(Integer)
    planet = relationship("Planet_To_Favorites")

class Vehicle(Base):
    __tablename__ = 'Vehicle'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    vehicle_name = Column(String(256))
    crew_size = Column(String(25))
    model = Column(String(256))
    cost_in_credits = Column(Float)
    consumables = Column(String(256))
    cargo_capacity = Column(Integer)
    length = Column(Float)
    manufacturer = Column(String(256))
    max_atmosphering_speed = Column(Integer)
    vehicle = relationship("Vehicle_To_Favorites")

class Person_To_Favorites(Base):
    __tablename__ = 'Person_To_Favorites'
    person_id = Column(Integer,ForeignKey("Person.id"),primary_key=True)
    user_id = Column(Integer,ForeignKey("User.id"),primary_key=True)

class Planet_To_Favorites(Base):
    __tablename__ = 'Planet_To_Favorites'
    planet_id = Column(Integer, ForeignKey("Planet.id"), primary_key=True)
    user_id = Column(Integer,ForeignKey("User.id"),primary_key=True)

class Vehicle_To_Favorites(Base):
    __tablename__ = 'Vehicle_To_Favorites'
    vehicle_id = Column(Integer, ForeignKey("Vehicle.id"), primary_key=True)
    user_id = Column(Integer,ForeignKey("User.id"),primary_key=True)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')