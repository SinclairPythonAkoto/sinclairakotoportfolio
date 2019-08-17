from flask import Flask, render_template, g, url_for, request, redirect

app = Flask(__name__)

from sqlalchemy.orm import sessionmaker, relationship

# # this part is needed to create session to query database.  this should be JUST BELOW app.config..
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, select
meta = MetaData()
engine = create_engine("postgresql://postgres:161086@localhost/test-db-01", echo = True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


if __name__ == '__main__':
	app.run(debug=True)
