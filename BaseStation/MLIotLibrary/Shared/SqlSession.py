__author__ = 'Stephen'
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine, )
from .Singleton import singleton

