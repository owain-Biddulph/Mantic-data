''' Methode 1, using political party with the most occurrances '''
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from creation_table_maire import Maires, Base
from flask import Flask, render_template

engine = create_engine('sqlite:///table_maires.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

list_political_parties = 

pages_web_1 = dict(zip(Maires.query(ID_maires).all, Maires,query(page_web_1).all()))
pages_web_2 = dict(zip(Maires.query(ID_maires).all:Maires,query(page_web_1).all()))
pages_web_3 = dict(zip(Maires.query(ID_maires).all:Maires,query(page_web_1).all()))


for maire in page_web_1 :
	max = 0
	max_party = None
	for party in list_political_parties :
		length = len(list_political_parties[party])
		occurrences = 0
		for el in range(length):
			occurrences += page_web_1[maire][el].count(party)
		if occurrences >= max :
			max = occurrences
			max_party = party
	update = update(Maires).where(ID_maire == maire).values(most_occurrences_1 = max_party)
	session.execute(update)

for maire in page_web_2 :
	max = 0
	max_party = None
	for party in list_political_parties :
		length = len(list_political_parties[party])
		occurrences = 0
		for el in range(length):
			occurrences += page_web_2[maire][el].count(party)
		if occurrences >= max :
			max = occurrences
			max_party = party
	update = update(Maires).where(ID_maire == maire).values(most_occurrences_2 = max_party)
	session.execute(update)

for maire in page_web_3 :
	max = 0
	max_party = None
	for party in list_political_parties :
		length = len(list_political_parties[party])
		occurrences = 0
		for el in range(length):
			occurrences += page_web_3[maire][el].count(party)
		if occurrences >= max :
			max = occurrences
			max_party = party
	update = update(Maires).where(ID_maire == maire).values(most_occurrences_3 = max_party)
	session.execute(update)		

session.commit()


