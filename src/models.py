import os
import sys
import enum

from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()



class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False, unique=True)

    person_favorite = relationship('Person_favorite', backref='user', lazy=True)
    planet_favorite = relationship('Planet_favorite', backref='user', lazy=True)
    vehicle_favorite = relationship('Vehicle_favorite', backref='user', lazy=True)
    

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(Integer, nullable=False)
    gender = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)

    person_favorite = relationship('Person_favorite', backref='person', lazy=True)


class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    vehicle_class = Column(String(250), nullable=False)
    length = Column(Integer, nullable=False)
    crew = Column(Integer, nullable=False)
    max_atmosphering_speed = Column(Integer, nullable=False)
    cargo_capacity  = Column(Integer, nullable=False)

    vehicle_favorite = relationship('Vehicle_favorite', backref='user', lazy=True)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    rotaion_period = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    
    planet_favorite = relationship('Planet_favorite', backref='planet', lazy=True)


class Person_favorite(Base):
    __tablename__ = 'person_favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'), nullable=False)

class Planet_favorite(Base):
    __tablename__ = 'planet_favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=False)

class Vehicle_favorite(Base):
    __tablename__ = 'vehicle_favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=False)
    


    # user_save_person = Column(Integer, ForeignKey('user.id'), primary_key=True)
    # user_save_vehicle = Column(Integer, ForeignKey('user.id'), primary_key=True)
    # user_save_planet = Column(Integer, ForeignKey('user.id'), primary_key=True)


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e