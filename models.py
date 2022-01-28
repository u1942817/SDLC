from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


posts = [
    {
        'author': 'Claudia Ellis',
        'title': 'Board 1',
        'content': 'First post content',
        'date_posted': 'January 17, 2022'
    },
    {
        'author': 'Ronnie Mather',
        'title': 'Post 2',
        'content': 'Second post content',
        'date_posted': 'January 20, 2022'
    }
]

@app.route('/')
def index():
    return render_template('homepage.html', title='Board Title', posts=posts)

@app.route('/homepage')
def homepage():
    return render_template('homepage.html', title='Homepage')

@app.route('/resource_board')
def resource_board():
    return render_template('resource_board.html', title='Resource Board')

@app.route('/login')
def login():
    return render_template('login.html', title='Login')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', title='Dashboard')

@app.route('/student_dashboard')
def student_dashboard():
    return render_template('student_dashboard.html', title='Student View')
    
if __name__ =='__main__':
    app.run(debug=True)  
