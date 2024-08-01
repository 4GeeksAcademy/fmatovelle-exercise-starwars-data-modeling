import os
import sys
import enum

from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# Definir el Enum para el campo 'type' en la clase 'Media'
# class MediaType(enum.Enum):  # Definimos un Enum con los valores posibles para 'type'
#     IMAGE = "image"
#     VIDEO = "video"
#     AUDIO = "audio"

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False, unique=True)
    
    person = relationship('Person', backref='user', lazy=True)
    vehicle = relationship('Vehicle', backref='user', lazy=True)
    planet = relationship('Planet', backref='user', lazy=True)
    favorite = relationship('Favorite', backref='user', lazy=True)
    # comments = relationship('Comment', backref='user', lazy=True)
    # followers = relationship('Follower', foreign_keys='Follower.user_to_id', backref='followed', lazy=True)
    # following = relationship('Follower', foreign_keys='Follower.user_from_id', backref='follower', lazy=True)

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(Integer, nullable=False)
    gender = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)



    # type = Column(Enum(MediaType), nullable=False)  # Usando el Enum definido
    # url = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)  # Agregamos la relación ForeignKey

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    vehicle_class = Column(String(250), nullable=False)
    length = Column(Integer, nullable=False)
    crew = Column(Integer, nullable=False)
    max_atmosphering_speed = Column(Integer, nullable=False)
    cargo_capacity  = Column(Integer, nullable=False)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    # post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    rotaion_period = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    
    # media = relationship('Media', backref='post', lazy=True)
    # comments = relationship('Comment', backref='post', lazy=True)


class Favorite(Base):
    __tablename__ = 'favorite'
    user_save_person = Column(Integer, ForeignKey('person.id'), primary_key=True)
    user_save_vehicle = Column(Integer, ForeignKey('vehicle.id'), primary_key=True)
    user_save_planet = Column(Integer, ForeignKey('planet.id'), primary_key=True)

    # user_from_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    # user_to_id = Column(Integer, ForeignKey('user.id'), primary_key=True)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e