#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
##__name__ is equal to the name of the module in question unless it is the module being run from the command line. In this case, it is set to '__main__'. 

##easiest way to define routes with Flask is through use of the @app.route decorator
##@app.route registers the index() function with the Flask application instance app. The @app.route() decorator is an instance method that modifies app, creating a rule that requests for the base URL (/) should show our index: a page with a header that says "Welcome to my app!"
@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

##run a development server through treating our application module as a script with the app.run() method below:
if __name__ == '__main__':
    app.run(port=5555, debug=True)