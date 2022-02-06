from SDLC.models import Post, User

def test_post():
    new_post = Post(title="Title", content="Content", user_id=1)
    assert new_post.title == "Title"
    assert new_post.content == "Content"
    assert new_post.user_id == 1

def test_user():
    new_user = User(username="Username", email="Email", password="Password")
    assert new_user.username == "Username"
    assert new_user.email == "Email"
    assert new_user.password == "Password"