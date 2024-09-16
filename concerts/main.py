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

# Creating the modals

class Band:
    __tablename__ = 'bands'
    id = Column(Integer() , primary_key = True)
    name = Column(String() , nullable = False)
    hometown = Column(String() , nullable = False)

    def __rep__(self):
        return f"<The Customer is : {self.name}>"
    
class Venue:
    __tablename__ = 'venues'
    id = Column(Integer() , primary_key = True)
    title = Column(String() , nullable = False)
    city = Column(String() , nullable = False)

    def __rep__(self):
        return f"<The Product is : {self.name}>"
