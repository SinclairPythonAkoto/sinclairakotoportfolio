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
class Contactme_Page(Base):
	__tablename__ = 'contactme_page'
	id = Column('id', Integer, primary_key=True)
	firstname = Column('firstname', String(15))
	lastname = Column('lastname', String(15))
	email = Column('email', String(30))
	exposure = Column('exposure', String(15))
	message = Column('message', String(800))
	
	def __init__(self, firstname, lastname, email, exposure, message):
		self.firstname = firstname
		self.lastname = lastname
		self.email = email
		self.exposure = exposure
		self.message = message

class Review_Page(Base):
	__tablename__ = 'review_page'
	id = Column('id', Integer, primary_key=True)
	firstname = Column('firstname', String(15))
	lastname = Column('lastname', String(15))
	email = Column('email', String(30))
	review_message = Column('review_message', String(800))

	def __init__(self, firstname, lastname, email, review_message):
		self.firstname = firstname
		self.lastname = lastname
		self.email = email
		self.review_message = review_message

class Feedback_Page(Base):
	__tablename__ = 'feedback_page'
	id = Column('id', primary_key=True)
	name = Column('name', String(20))
	experience = Column('experience', String(12))
	functionality = Column('functionality', String(12))
	aesthetics = Column('aesthetics', String(12))
	my_cv = Column('my_cv', String(12))
	my_webapp = Column('my_webapp', String(12))
	outstanding = Column('outstanding', String(15))
	improve = Column('improve', String(15))
	email = Column('email', String(30))

	def __init__(self, name, experience, functionality, aesthetics, my_cv, my_webapp, outstanding, improve, email):
		self.name = name
		self.experience = experience
		self.functionality = functionality
		self.aesthetics = aesthetics
		self.my_cv = my_cv
		self.my_webapp = my_webapp
		self.outstanding = outstanding
		self.improve = improve
		self.email = email


Session = sessionmaker(bind=engine)
# Session = sessionmaker(autoflush=True)
session = Session()

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

@app.route('/aboutme')
def aboutme():
	return render_template('aboutme.html')

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/cv')
def cv():
	return render_template('cv.html')

@app.route('/apps')
def web_apps():
	return render_template('web_apps.html')

@app.route('/review', methods=['GET', 'POST'])
def review():
	if request.method == 'GET':
		return render_template('review.html')
	else:
		firstname = request.form.get('firstname')
		lastname = request.form.get('lastname')
		email = request.form.get('email')
		review_message = request.form.get('subject')

		db_data = Review_Page(firstname, lastname, email, review_message)
		session.add(db_data)
		session.commit()
		data = session.query(Review_Page).all()

		return render_template('review.html', data=data)

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
	if request.method == 'GET':
		return render_template('feedback.html')
	else:
		name = request.form.get('name')
		experience = request.form.get('experience')
		functionality = request.form.get('functionality')
		aesthetics = request.form.get('aesthetics')
		my_cv = request.form.get('my_cv')
		my_webapp = request.form.get('my_webapp')
		outstanding = request.form.get('outstanding')
		improve = request.form.get('improve')
		email = request.form.get('email')

		db_data = Feedback_Page(name, experience, functionality, aesthetics, my_cv, my_webapp, outstanding, improve, email)
		session.add(db_data)
		session.commit()
		data = session.query(Feedback_Page).all()

		return render_template('feedback.html', data=data)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
	if request.method == 'GET':
		return render_template('contact.html')
	else:
		firstname = request.form.get('firstname')
		lastname = request.form.get('lastname')
		email = request.form.get('email')
		exposure = request.form.get('exposure')
		message = request.form.get('subject')
		viewAll_db = request.form.get('viewAll')

		db_data = Contactme_Page(firstname, lastname, email, exposure, message)
		session.add(db_data)
		session.commit()	
		data = session.query(Contactme_Page).all()

		if request.form.get('viewAll_btn'):
			return render_template('contact.html', data=data, viewAll_db=viewAll_db)
		return render_template('contact.html', data=data, viewAll_db=viewAll_db)

@app.route('/interactive')
def interactive():
	return render_template('interactive.html')

if __name__ == '__main__':
	app.run(debug=True)
