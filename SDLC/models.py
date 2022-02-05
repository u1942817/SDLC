from datetime import datetime
from SDLC import db, login_manager
from flask_login import UserMixin
import os


@login_manager.user_loader # decorator allows the modification of function (in routes.py)
def load_user(user_id):
    return User.query.get(int(user_id)) # query the user_id from the db


class User(db.Model, UserMixin): # UserMixin allows for the get_id() from the decorator above 
    id = db.Column(db.Integer, primary_key=True) #the user id is the primary key and can only be an integer
    username = db.Column(db.String(20), unique=True, nullable=False) # username is a string, must be filled out and can only contain a max of 20 characters 
    email = db.Column(db.String(120), unique=True, nullable=False) 
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg') # the image file has been prepared for future improvements 
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True) # this represents the relationship between the User and the Post 

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')" # when querying the db, these are the only fields that will be returned (due to security)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True) # the user id is the primary key and can only be an integer
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) # date posted uses the DateTime module respective of the current local time of the user
    content = db.Column(db.Text, nullable=False) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # this represents the field that is used to connect to the User models (the foreign key)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

''''
from routes import file_upload

@file_upload.Model
class blogModel(db.Model):
   __tablename__ = "blogs"
   id = db.Column(db.Integer, primary_key=True)

   # Use flask-file-upload's `file_upload.Column()` to associate a file with a SQLAlchemy Model:
   my_placeholder = file_upload.Column()
   my_video = file_upload.Column()'''