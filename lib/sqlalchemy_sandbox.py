#!/usr/bin/env python3
##The declarative_base combines a container for table metadata 
#as well as a group of methods that act as mappers between Python and our SQL database.
#Inheritance from Base, a declarative_base object, allows us to avoid rewriting code.

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    pass

if __name__ == '__main__':
    ##data models
    
    engine = create_engine('sqlite:///students.db', echo=True)
    Base.metadata.create_all(engine)

    pass