'''
This is a "hello world" flask webpage.
During the last 2 weeks of class,
we will be modifying this file to demonstrate all of flask's capabilities.
This file will also serve as "starter code" for your Project 5 Twitter webpage.

NOTE:
the module flask is not built-in to python,
so you must run pip install in order to get it.
After doing do, this file should "just work".
'''

import sqlite3
from flask import Flask, render_template, request
app = Flask(__name__)

# Anything that starts with a @ is called a "decorator" in python.
# Decorators modify the functions that follow them.
# The flask library uses decorators to convert functions into *routes*.
# A route is a *path* that is visible in the web server.
@app.route('/')
def root():

    # first construct a [{}]
    # that contains the info about the messages
    messages = [
        {'username': 'Mike', 'text': 'hello world'},
        {'username': 'Mike', 'text': 'hola mundo'},
        {'username': 'Trump', 'text': 'derpity derp'},
    ]
    # last step to get this to work is to:
    # load the messages list from the database

    return render_template('index.html', messages=messages)


def verify_login_info():
    '''
    Return True if the user is correctly logged in.
    '''
    # Do the username/password checks.
    username = request.args.get('username')
    print('username=', username)
    password = request.args.get('password')
    print('password=', password)

    login_successful = False
    con = sqlite3.connect('twitter_clone.db')
    cur = con.cursor()
    sql = """
    SELECT password, id FROM users WHERE username=?;
    """
    cur.execute(sql, [username])
    for row in cur.fetchall():
        print('row[0]=', row[0])
        if password == row[0]:
            login_successful = True
            print('login_successful = True')


    '''
    if username == 'Mike' and password == '123':
        login_successful = True
    '''

    return username, password, login_successful


@app.route('/login')
def login():
    # the request.args.get will give us the query parameters
    # NOTE:
    # request (singular) use in flask to process the query args
    # requests (plural) download from the internet

    username, password, login_successful = verify_login_info()

    if username is None and password is None:
        tried_to_login = False
    else:
        tried_to_login = True

    return render_template(
        'login.html', 
        login_successful=login_successful,
        tried_to_login=tried_to_login,
        )

@app.route('/logout')
def logout():
    return render_template('logout.html')

# urls have the form of scheme://hostname/route
# scheme = http
# hostname = 127.0.0.1:5000
# route = /example
@app.route('/example')
def example():
    text = 'example'
    return text

app.run()
