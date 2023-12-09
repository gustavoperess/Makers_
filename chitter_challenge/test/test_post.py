from lib.post import *

def test_user():
    user = Post(1, "title", "content" , "234", "User_id")
    assert user.id == 1
    assert user.title == "title"
    assert user.content == "content"
    assert user.number_views == "234"
    assert user.user_id == "User_id"