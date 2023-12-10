Chitter Social Media Platform Documentation

Overview
Chitter is a simple social media platform built using Python and the Flask web framework. It provides basic user authentication,
allowing users to register, log in, create posts, and delete their own posts.

![Screenshot 2023-12-10 at 6 50 45 PM](https://github.com/gustavoperess/Makers_/assets/32426662/28cdb578-fb10-4246-ae93-80b3a9cc464d)

Technologies Used
Languages:
Python

Frameworks:
Flask
Flask-Login
Flask-Bcrypt

Database:
PostgressSQL

Setup - Prerequisites
```
# Install dependencies:
pip install -r requirements.txt

#Set up the Flask application
export FLASK_APP=app.py
export FLASK_ENV=development  # Optional: enables development mode with debug features

# Run the application:
flask run

```
Below is the user story

```
As a Maker
So that I can let people know what I am doing
I want to post a message (peep) to chitter

As a maker
So that I can see what others are saying
I want to see all peeps in reverse chronological order

As a Maker
So that I can better appreciate the context of a peep
I want to see the time at which it was made

As a Maker
So that I can post messages on Chitter as me
I want to sign up for Chitter

As a Maker
So that only I can post messages on Chitter as me
I want to log in to Chitter

As a Maker
So that I can avoid others posting messages on Chitter as me
I want to log out of Chitter

FUTURE FETURE

As a Maker
So that I can stay constantly tapped in to the shouty box of Chitter
I want to receive an email if I am tagged in a Peep
```
