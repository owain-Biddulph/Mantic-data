import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, update
from creation_table_maire import Maires, Base
from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

engine = create_engine('sqlite:///table_maires.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

id_maire = 0
f = open('maires.txt', 'r')
for line in f:
    id_maire +=1
    insee_code = line.split(';')[0]
    department = line.split(';')[1]
    commun = line.split(';')[2]
    population = line.split(';')[3]
    maire_surname = line.split(';')[4]
    maire_firstname = line.split(';')[5]
    maire_sex = line.split(';')[6]
    maire_birth_date = line.split(';')[7]
    maire_csp = line.split(';')[8]
    csp_title = line.split(';')[9]
    session.add(
        Maires(ID_maire = id_maire,
            insee_code=insee_code.strip('"'),
            department=department.strip('"'),
            commun=commun.strip('"'),
            population=population,
            maire_surname=maire_surname.strip('"'),
            maire_firstname=maire_firstname.strip('"'),
            maire_sex=maire_sex.strip('"'),
            maire_birth_date=maire_birth_date,
            maire_csp=maire_csp,
            csp_title=csp_title.strip('"')))

session.commit()



def raw_scraping(commun, surname, firstname):
    r = requests.get("https://www.google.fr/search?q={}+{}+{}".format(commun, surname, firstname))
    soup = BeautifulSoup(r.text, "html.parser")

    head3 = soup.find_all("h3", class_="r", limit=4)
    urls = []
    raw = []

    for title in head3[1:]:
        link = title.a['href']
        urls.append(link.split('&')[0][7:])

    for url in urls:
        try :
            r = requests.get(url)
        except :
            raw.append('')
        soup = BeautifulSoup(r.text, "html.parser")
        try :
            string = soup.body.text
        except :
            string = ''
        raw.append(string)
    return raw


for maire in session.query(Maires).all() :
    pages = raw_scraping(maire.commun, maire.maire_surname, maire.maire_firstname)
    update = Maires.__table__.update().where(Maires.ID_maire == maire.ID_maire).values(web_page_1 = pages[0], web_page_2 = pages[1], web_page_3 = pages[2])
    session.execute(update)

session.commit()

f.close()

@app.route('/')
def index():
    return render_template(
        'show_all.html', Maires=session.query(Maires).all())


if __name__ == '__main__':
    app.run()
