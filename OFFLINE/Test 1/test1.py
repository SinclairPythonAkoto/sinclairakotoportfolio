from flask import Flask, render_template, g, url_for, request, redirect

app = Flask(__name__)

from sqlalchemy.orm import sessionmaker, relationship

# # this part is needed to create session to query database.  this should be JUST BELOW app.config..
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, select
meta = MetaData()
engine = create_engine("postgresql://postgres:161086@localhost/test-db-01", echo = True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# BUILD DATABASE CLASS HERE

@app.route('/')
def intro1():
	return render_template('intro1.html')

@app.route('/intro2')
def intro2():
	return render_template('intro2.html')

@app.route('/intro3')
def intro3():
	return render_template('intro3.html')

@app.route('/intro4')
def intro4():
	return render_template('intro4.html')

@app.route('/intro5')
def intro5():
	return render_template('intro5.html')

@app.route('/intro6')
def intro6():
	return render_template('intro6.html')

@app.route('/intro7')
def intro7():
	return render_template('intro7.html')

@app.route('/home')
def home():
	return "Hello World!"





if __name__ == '__main__':
	app.run(debug=True)
