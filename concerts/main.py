import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String
)

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connection_str = 'sqlite:///' + os.join(BASE_DIR , 'concert.db')

engine = create_engine(connection_str)

Base = declarative_base()

'''
class Band:
    id : int pk
    name : str
    hometown : str

class venue:
    id : int pk
    title : str
    city : str

#Association table (concerts)
    band_id : int fk(bands.id)
    venue_id : int fk(venues.id)
'''