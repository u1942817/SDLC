from flask import render_template, url_for, flash, redirect
from SDLC import app, db
from SDLC.forms import RegistrationForm, LoginForm, PostForm, UpdateAccountForm
from SDLC.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route("/homepage")
def homepage():
    posts= Post.query.all()
    return render_template('homepage.html', title='Board Title', posts=posts)


@app.route('/resource_board')
def resource_board():
    return render_template('resource_board.html', title='Resource Board')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created, you are now able to login! ', 'success')
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first() # finds the first (and only) user with that email
        if user:
            login_user(user, remember=form.remember.data)
            return redirect(url_for('homepage'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
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

@app.route('/dashboard/new', methods=['GET', 'POST'])
def dashboard():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Post has been created', 'success')
        return redirect(url_for('resource_board'))
    return render_template('dashboard.html', title='Dashboard', form=form, legend='New Post')


@app.route('/student_dashboard')
def student_dashboard():
    return render_template('student_dashboard.html', title='Student View')