import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from bs4 import BeautifulSoup
import requests

Base = declarative_base()

class Maires_wiki(Base):
    __tablename__ = 'maires_wiki'
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
    political_party = Column(String(250), default = 'empty')

engine = create_engine('sqlite:///table_maires_wiki.db')

Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)

session = DBSession()

# id_maire = 0
# f = open('maires.txt', 'r')
# for line in f:
#     id_maire +=1
#     insee_code = line.split(';')[0]
#     department = line.split(';')[1]
#     commun = line.split(';')[2]
#     population = line.split(';')[3]
#     maire_surname = line.split(';')[4]
#     maire_firstname = line.split(';')[5]
#     maire_sex = line.split(';')[6]
#     maire_birth_date = line.split(';')[7]
#     maire_csp = line.split(';')[8]
#     csp_title = line.split(';')[9]
#     session.add(
#         Maires_wiki(ID_maire = id_maire,
#             insee_code=insee_code.strip('"'),
#             department=department.strip('"'),
#             commun=commun.strip('"'),
#             population=population,
#             maire_surname=maire_surname.strip('"'),
#             maire_firstname=maire_firstname.strip('"'),
#             maire_sex=maire_sex.strip('"'),
#             maire_birth_date=maire_birth_date,
#             maire_csp=maire_csp,
#             csp_title=csp_title.strip('"')))

# session.commit()

for maire in session.query(Maires_wiki).filter(Maires_wiki.ID_maire <= 200).filter(Maires_wiki.ID_maire >= 50) :
    surname = maire.maire_surname[0]+maire.maire_surname.lower()[1:]
    try:
        r = requests.get("https://en.wikipedia.org/wiki/{}".format(str(maire.maire_firstname) + "_" + surname))
    except:
        print("page doesn't exist")
        continue
    soup = BeautifulSoup(r.text, "html.parser")
    head = soup.find("th", text = "Parti politique")
    try:
        parent_tag = head.parent
    except :
        print('empty')
        continue
    parties = head.findNext('td')
    party = parties.find_all('a')[-1].text
    print(party)
