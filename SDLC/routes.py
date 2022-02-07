from flask import render_template, url_for, flash, redirect, request
from SDLC import app, db
from SDLC.forms import RegistrationForm, LoginForm, PostForm
from SDLC.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
import os

@app.route('/')
@app.route("/homepage")
def homepage():
    return render_template('homepage.html', title='Board Title')

@app.route('/dashboard', methods=['GET', 'POST']) # the app looks for the /dashboard url and uses the 'GET' and 'POST' methods
def dashboard():
    form = PostForm() # form is equal to the form created in forms.py
    posts = Post.query.order_by(Post.date_posted).all() # post is equal to all attritbues within the Post model ordered by the date created
    if form.validate_on_submit(): # the form must be validated from wtforms.validators
        post = Post(title=form.title.data, content=form.content.data, user_id=current_user) # post data is filled out, title, content and author 
        db.session.add(post) # this is added to the database to be stored
        db.session.commit() # in order to successfully store the data, a commit has to take place
        flash('Post has been created', 'success') # this provides the user a visual that the post has been successfully made
        return redirect(url_for('posts')) 
    return render_template('dashboard.html', title='Dashboard', form=form, posts=posts, legend='New Post') # the app returns the dashboard.html

@app.route('/resource_board') # the app looks for the /resource board url
def posts():
    files = os.listdir(app.config['UPLOAD_PATH']) # files is used to find the correct path from the __init__ file
    posts = Post.query.order_by(Post.date_posted).all() # all posts are queried and ordered by date posted and referenced by {%for file in files %} in refernece board html
    for post in posts: # this checks that the posts have been identified and ordered
        print(post.id)
    return render_template('resource_board.html', posts=posts, files=files)

@app.route("/resource_board", methods=["GET", "POST"]) # the app looks for the /resource board url and uses the 'GET' and 'POST' methods
def upload_files():
    if request.method == 'POST':
        file = request.files["file"] 
        print(file)
        return redirect(url_for('dashboard'))
    files = os.listdir(app.config['UPLOAD_PATH']) # files is used to find the correct path from the __init__ file
    print(files)
    return render_template("resource_board.html", files=files)

@app.route("/register", methods=['GET', 'POST']) # the app looks for the /register url and uses the 'GET' and 'POST' methods
def register():
    if current_user.is_authenticated: # a user is authenticated once a valid form ahs been submitted 
        return redirect(url_for('homepage')) # the user is redirected to the homepage of WMGTSS
    form = RegistrationForm() # form is equal to the form created in the form.py file, this is the structure for the form
    if form.validate_on_submit(): # the form must be validated on submit which uses ValidationError from the RegistrationForm()
        user = User(username=form.username.data, email=form.email.data, password=form.password.data) # the user is defined by the data given in the form
        db.session.add(user) # the system add this to store in the db
        db.session.commit() # in order to store, the data must be committed
        flash('Your account has been created, you are now able to login! ', 'success') # a message will display to the user to inform that they have made an account
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: # when the current user is authenticated through login, direct them to the homepage
        return redirect(url_for('homepage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first() # finds the first (and only) user with that email
        if user.password==form.password.data: # if password is the same as the password in the database direct them to the homepage 
            login_user(user, remember=form.remember.data)
            return redirect(url_for('homepage'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger') #  if login username or password is incorrect, flash a login unsuccessful message
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for ('homepage'))

@app.route("/account")
@login_required # this ensures the user logins before accessing this page
def account():
    form = PostForm()
    return render_template('account.html', title='Account', form=form)



