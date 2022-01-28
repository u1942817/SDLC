from flask import Flask
from flask import render_template
from enum import unique
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), nullable = False, unique= True)
    password = db.Column(db.String(50), nullable = False)
    first_name = db.Column(db.String(100), nullable = False)
    surname = db.Column(db.String(100), nullable = False)
    type =db.Column(db.String(50), nullable = False)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///RB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db.init_app(app)

@app.route('/')
def index():
    return render_template('homepage.html', title='Board Title')

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/resource_board')
def resource_board():
    return render_template('resource_board.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
    
    
if __name__ =='__main__':
    app.run(debug=True)  

    