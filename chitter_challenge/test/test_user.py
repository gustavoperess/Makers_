from lib.user import User

def test_user():
    user = User(1,"Gustavo","Gustavo123")
    assert user.id == 1
    assert user.user_name == "Gustavo"
    assert user.user_password == "Gustavo123"

def test_user_formated_nicetly():
    user = User(1,"Gustavo","Gustavo123")
    assert str(user) == "User(1, Gustavo, Gustavo123)"