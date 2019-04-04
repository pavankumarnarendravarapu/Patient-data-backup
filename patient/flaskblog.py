#from datetime import datetime
from flask import Flask,render_template,url_for,flash,redirect, request
from hospital_database import Hospital, Patient, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#from flask_bootstrap import Bootstrap
#from flask_wtf import FlaskForm
#from wtforms import StringField, PasswordField
#from wtforms.validators import InputRequired, Email, Length
engine = create_engine('sqlite:///patientdata.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#Flask is a class name in flask
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm,LoginForm
app=Flask(__name__)

#Bootstrap(app)

#class LoginForm(FlaskForm):
    #username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    #password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

#__name__ is a special variable in python and app is a variable

#SECRET KEY
app.config['SECRET_KEY']='d54a02195cc5c67ed3155bd20fbf0949'
#DB SQLALCHEMY
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

#its is represents the database struct
db= SQLAlchemy(app)

#class RegistrationForm(FlaskForm):
    #email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    #username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    #password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

@app.route("/") #dir #localhost:5000/
@app.route("/home")#localhost:5000/home
def home():
    return render_template('home.html')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'pavan@gmail.com' and form.password.data == 'password':
            #email = request.form.get("email")
            #password = request.form.get("password")
            flash('You have been logged in!', 'success')
            return redirect(url_for('check'))
        else:
            flash('Login Unsuccessful. please check username and password', 'danger')
    return render_template('login.html', form=form)
 
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form )

@app.route('/check', methods=['POST', 'GET'])
def check():
    if request.method == "POST":
        pat = session.query(Patient).filter_by(name = request.form['name']).first()
        session.close()
        return render_template('check.html', pat=pat)
    else:
        pat = session.query(Patient).all()
        session.close()
        return render_template('check.html', pat="no data")


@app.route('/data', methods=['POST', 'GET'])
def data():
    if request.method == 'POST':
        newList = Patient(
            name = request.form['name'],
            age = request.form['age'],
            disease = request.form['disease'],
            health_cond = request.form['health_cond'],
            bill = request.form['bill'],
            type_of_drug = request.form['type_of_drug'],
            drug_quant = request.form['drug_quant'],
            cost = request.form['cost'],
            village = request.form['village'],
            phone = request.form['phone'],
            address = request.form['address'])
        session.add(newList)
        session.commit()
        return redirect(url_for('data'))
    else:
        return render_template('data.html')


@app.route('/dia')
def dia():
    return render_template('dia.html')


@app.route('/imp')
def imp():
    return render_template('imp.html')


@app.route('/card')
def card():
    return render_template('card.html')


@app.route('/int')
def int():
    return render_template('in.html')

@app.route('/eme')
def eme():
    return render_template('eme.html')


@app.route('/med')
def med():
    return render_template('med.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/openinghours')
def openinghours():
    return render_template('openinghours.html')

@app.route('/services')
def services():
    return render_template('services.html')


#another way to run the server without using flask run command
#but here we can dirctly run server as filename that is python flaskblog.py

if __name__== '__main__':
    app.run(debug=True)

