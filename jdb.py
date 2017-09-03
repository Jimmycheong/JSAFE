'''
This file contains the Schema for the master password and user password hashes.

Ensure all dependancies are installed via the requirements.txt.
'''

from sqlalchemy import Column, Integer, String, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Epasswords(Base):
    '''
    User password Schema

    Future columns: Date stored, email

    '''
    __tablename__ = 'epasswords'

    id = Column(Integer, primary_key=True)
    company = Column(String(80), nullable=False)
    username = Column(String(100))
    password = Column(LargeBinary(400))


class Hasht(Base):
    '''
    Master password Schema
    '''
    __tablename__ = 'hasht'

    id = Column(Integer, primary_key=True)
    hash = Column(LargeBinary(400))

ENGINE = create_engine('sqlite:///storage.db')
Base.metadata.create_all(ENGINE)
