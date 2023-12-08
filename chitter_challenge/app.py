import os
from flask import Flask, render_template, request, redirect, url_for
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.user import User
from lib.forms import LoginForm, RegisterForm
from flask_bcrypt import Bcrypt


app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] = 'thisisasecretkey'


@app.route('/', methods=['GET'])
def main_page():
    form = LoginForm()
    return render_template('index.html', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login_page():
    return render_template('login.html')



@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        connection = get_flask_database_connection(app)
        repository = UserRepository(connection)
        hashed_password = bcrypt.generate_password_hash(form.password.data) 
        new_user = User(None, user_name=form.username.data, user_password=hashed_password)
        repository.create(new_user)
        return redirect(url_for('main_page'))
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))