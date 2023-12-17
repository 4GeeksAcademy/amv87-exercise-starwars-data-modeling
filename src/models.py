import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    subscription_date = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    surname = Column(String(250), nullable=False)
    favorite_characters = relationship('FavoriteCharacter', back_populates='character')
    favorite_planets = relationship('FavoritePlanet', back_populates='planet')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    mass = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    favorite_characters = relationship('FavoriteCharacter', back_populates='character')

class FavoriteCharacters(Base):
    __tablename__ = 'favorite_characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='favorite_characters')
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship('Character', back_populates='favorite_characters')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    rotation_period = Column(String(250), nullable=False)
    orbital_period = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    surface_water = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    favorite_planets = relationship('FavoritePlanet', back_populates='planet')

class FavoritePlanets(Base):
    __tablename__ = 'favorite_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='favorite_planets')
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship('Planet', back_populates='favorite_planets')

render_er(Base, 'diagram.png')
