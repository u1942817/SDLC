from SDLC.models import Post, User # import User and POst class from models 

# a new post will be mocked with the title and content strings if it passes
def test_post():
    new_post = Post(title="Title", content="Content", user_id=1) 
    assert new_post.title == "Title"
    assert new_post.content == "Content"
    assert new_post.user_id == 1

# a new user will be mocked to the db with the username, email and password strings is it passes
def test_user():
    new_user = User(username="Username", email="Email", password="Password")
    assert new_user.username == "Username"
    assert new_user.email == "Email"
    assert new_user.password == "Password"