'''from flask import render_template, url_for, flash, redirect, request, Response
#from flask_dropzone import Dropzone
from SDLC import app, db
from SDLC.forms import RegistrationForm, LoginForm, PostForm
from SDLC.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.utils import secure_filename
import os
#from flask import send_from_directory
#import imghdr

@app.route('/')
@app.route("/homepage")
def homepage():
    return render_template('homepage.html', title='Board Title')

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

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    form = PostForm()
    if form.validate_on_submit():
        #file = form.file.data # grabs the file
        #file.save(os.path.join(app.config['UPLOADED_FOLDER'], file.filename))#saves the file
        form = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(form)
        db.session.commit() 
        flash('Post has been created', 'success')
        return redirect(url_for('posts'))
    return render_template('dashboard.html', title='Dashboard', form=form, legend='New Post')


@app.route('/resource_board')
def posts():
    posts = Post.query.order_by(Post.date_posted).all()
    for post in posts:
        print(post.id)
    return render_template('resource_board.html', posts=posts)


def validate_image(stream):
    header = stream.read(512)  # 512 bytes should be enough for a header check
    stream.seek(0)  # reset stream pointer
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')

@app.errorhandler(413)
def too_large(e):
    return "File is too large", 413 

@app.route('/resource_board')
def posts():
    posts = Post.query.order_by(Post.date_posted).all()
    for post in posts:
        print(post.id)
    return render_template('resource_board.html', posts=posts)

@app.route('/resource_board/files', methods=['POST'])
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    filename = secure_filename(uploaded_file.filename)
    uploaded_file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(uploaded_file.filename)))
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
                file_ext != validate_image(uploaded_file.stream):
            return "Invalid image", 400
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    return redirect(url_for('dashboard'))

@app.route('/documents/<filename>')
@login_required
def upload(filename):
    return send_from_directory(os.path.join(
        app.config['UPLOAD_PATH'], current_user.get_id()), filename)



dropzone = Dropzone(app)
@app.route('/resource_board/files', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join(app.config['UPLOADED_FOLDER'], f.filename))
    return render_template('resource_board.html')

@app.route('/resource_board')
def posts():
    posts = Post.query.order_by(Post.date_posted).all()
    for post in posts:
        print(post.id)
    return render_template('resource_board.html', posts=posts) 

@app.route('/resource_board/upload', methods=['POST'])
def upload():
    pic = request.files['pic']
    if not pic:
        return 'No pic uploaded!', 400

    filename = secure_filename(pic.filename)
    mimetype = pic.mimetype
    if not filename or not mimetype:
        return 'Bad upload!', 400

    img = Post(img=pic.read(), name=filename, mimetype=mimetype)
    db.session.add(img)
    db.session.commit()

    return 'Img Uploaded!', 200


@app.route('/<int:id>')
def get_img(id):
    img = Post.query.filter_by(id=id).first()
    if not img:
        return 'Img Not Found!', 404

    return Response(img.img, mimetype=img.mimetype)

@app.route('/student_dashboard')
def student_dashboard():
    return render_template('student_dashboard.html', title='Student View')'''


    #---------------------------------------------------
from flask import render_template, url_for, flash, redirect, request
from SDLC import app, db
from SDLC.forms import RegistrationForm, LoginForm, PostForm
from SDLC.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.utils import secure_filename
import os

@app.route('/')
@app.route("/homepage")
def homepage():
    posts= Post.query.all()
    return render_template('homepage.html', title='Board Title', posts=posts)

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

@app.route('/dashboard', methods=['GET', 'POST']) 
def dashboard():
    form = PostForm()
    posts = Post.query.order_by(Post.date_posted).all()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Post has been created', 'success')
        return redirect(url_for('posts'))
    return render_template('dashboard.html', title='Dashboard', form=form, posts=posts, legend='New Post')

@app.route('/resource_board')
def posts():
    posts = Post.query.order_by(Post.date_posted).all()
    for post in posts:
        print(post.id)
    return render_template('resource_board.html', posts=posts)

@app.route("/resource_board/upload", methods=["GET", "POST"])
def upload():
    if request.method == 'POST':
        file = request.files["file"]
        print(file)
        return redirect(request.url)
    return render_template("resource_board.html")
