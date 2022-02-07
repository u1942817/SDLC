from flask_wtf import FlaskForm # imports Flask Form for login and regsiter
from flask_login import current_user # this identifies the current user logged in and assigns the post creator to them 
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, FileField # used to create forms for the login/register and posts
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired # used to validate the form fields, ensure that fields are in correct format etc
from flask_wtf.file import FileField, FileAllowed # used to upload files and ensure they are correct format 
from SDLC.models import User # import the User class from models 



class RegistrationForm(FlaskForm): # FlaskForm is used for the registeration form imported from wtforms
    username = StringField('Username', 
                           validators=[DataRequired(), Length(min=2, max=20)]) # when filling out the forms, the user must fill out a username between 2-20 characters 
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username): # this notifies the user that the specific username has been taken
        user = User.query.filter_by(username=username.data).first() # in order to validate, the db must query the first name 
                                                                            #that appears that matches the username entered 
        if user: # if so, the user is prompted to enter another username 
            raise ValidationError('That username is taken, please choose another one.')
    
    def validate_email(self, email): # this notifies the user that the specific email has been taken
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken, please choose another one.')


class LoginForm(FlaskForm):# FlaskForm is used for the login form imported from wtforms
    email = StringField('Email',
                        validators=[DataRequired(), Email()]) # when filling out the form, the user must fill out a valid email address
    password = PasswordField('Password', validators=[DataRequired()]) # the password must match the one stored in the database that matches the email 
    remember = BooleanField('Remember Me') # allows for the users data to be remembered for easy login
    submit = SubmitField('Login')

class PostForm(FlaskForm): # PostForm is used when the user wants to create a post
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class UploadFileForm(FlaskForm): # UploadFileForm is used when the user wants to upload a file to the post/board
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")


class UpdateAccountForm(FlaskForm): # This has been inserted as a placeholder for when profile settings are created
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')


