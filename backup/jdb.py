import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm	import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Epasswords(Base):

	__tablename__ = 'epasswords'

	id = Column(Integer, primary_key = True)
	company = Column(String(80), nullable = False)
	username = Column(String(100))
	password = Column(LargeBinary(400))

	#Future columns: Date stored, email,

class Hasht(Base):

	__tablename__ = 'hasht'

	id = Column(Integer, primary_key = True)
	hash = Column(LargeBinary(400))

engine = create_engine('sqlite:///storage.db')
Base.metadata.create_all(engine) 