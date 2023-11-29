from lib.user import *

def test_user():
    user = User(1, "user@gmail.com", "user123")
    assert user.id == 1
    assert user.email == "user@gmail.com"
    assert user.name == "user123"