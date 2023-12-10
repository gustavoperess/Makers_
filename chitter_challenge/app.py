import os
from flask import Flask, render_template, request, redirect, url_for, flash
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.post_repository import PostRepository
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from lib.user import User
from lib.forms import LoginForm, RegisterForm
from flask_bcrypt import Bcrypt


app = Flask(__name__, static_url_path='/static')
bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] = 'thisisasecretkey'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login_page"

@login_manager.user_loader
def load_user(user_id):
    connection = get_flask_database_connection(app)
    
    # Load user information
    user_repository = UserRepository(connection)
    user = user_repository.find(int(user_id))

    # Load post information
    post_repository = PostRepository(connection)
    posts = post_repository.find_all_posts_by_user(int(user_id))
    
    if user:
        user.posts = posts
    
    return user

@app.route('/', methods=['GET', 'POST'])
def main_page():
    form = LoginForm()
    if form.validate_on_submit():
        connection = get_flask_database_connection(app)
        repository = UserRepository(connection)
        user = repository.find_by_name(form.username.data)
        if user and bcrypt.check_password_hash(user.user_password.encode('utf-8'), form.password.data.encode('utf-8')):
                login_user(user)      
                return redirect(url_for('login_page'))
        else:
            flash("User not in the system")
    return render_template('index.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
@login_required
def login_page():
    
    if not current_user.posts:
        flash("User does not have any posts yet")
        
    return render_template('login.html', user=current_user)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('main_page'))


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        connection = get_flask_database_connection(app)
        repository = UserRepository(connection)
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(None, user_name=form.username.data, user_password=hashed_password)
        success, user = repository.create(new_user)
        print(success)
        if success:
            flash("Registration successful")
            return redirect(url_for('main_page'))
        else:
            flash("Username already exists. Please choose a different username.")
    return render_template('register.html', form=form)



if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))