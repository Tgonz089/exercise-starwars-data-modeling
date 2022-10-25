import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
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

class Planet(Base):
    __tablename__ = 'Planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_fav_id = Column(Integer)
    planet_name = Column(String(256))
    population = Column(String(256))
    terrain = Column(String(25))

class Vehicle(Base):
    __tablename__ = 'Vehicle'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    vehicle_name = Column(String(256))
    crew_size = Column(String(25))
    model = Column(String(256))


class Favorites(Base):
    __tablename__ = 'Favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    User_id = Column(Integer, ForeignKey('User.id'))
    Person_fav_id = Column(Integer, ForeignKey('Person.id'))
    Planet_fav_id = Column(Integer, ForeignKey('Planet.id'))
    Vehicle_fav_id = Column(Integer, ForeignKey('Vehicle.id'))
    Person = relationship(Person)
    Vehicle = relationship(Vehicle)
    Planet = relationship(Planet)
    User = relationship(User)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')