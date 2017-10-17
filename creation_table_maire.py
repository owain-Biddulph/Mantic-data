import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Maires(Base):
    __tablename__ = 'Maires'
    ID_maire = Column(Integer, primary_key = True)
    insee_code = Column(String(250))
    department = Column(String(250))
    commun = Column(String(250))
    population = Column(Integer)
    maire_surname = Column(String(250))
    maire_firstname = Column(String(250))
    maire_sex = Column(String(250))
    maire_birth_date = Column(String(250))
    maire_csp = Column(Integer)
    csp_title = Column(String(250))
    web_page_1 = Column(String(300000), default = 'empty')
    web_page_2 = Column(String(300000), default = 'empty')
    web_page_3 = Column(String(300000), default = 'empty')
    most_occurrences_1 = Column(String(250), default = 'empty')
    most_occurrences_2 = Column(String(250), default = 'empty')
    most_occurrences_3 = Column(String(250), default = 'empty')
    political_orientation = Column(String(250), default = 'empty')

engine = create_engine('sqlite:///table_maires.db')

Base.metadata.create_all(engine)