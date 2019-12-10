from app import app

from flask import request, render_template, send_from_directory, make_response
import datetime
import sqlite3

# decorator
@app.route('/')
def hello():
    # STEP 1: get the info from sqlite
    connection = sqlite3.connect(
        'twitter_clone.db'
        )
    # twitter_clone.db.journal
    # twitter_clone.db.wal
    cursor = connection.cursor()
    sql = '''
        SELECT * FROM messages;
    '''
    res = cursor.execute(sql)
    rows = res.fetchall()
    messages = []
    for row in rows:
        message = {}
        message['sender'] = row[1] # sender
        message['message'] = row[2] # message
        message['timestamp'] = row[3] # timestamp
        messages.append(message)

    messages_static = [
        { 'sender' : 'mike',
          'message' : 'Hello world!',
          'timestamp' : datetime.datetime.now()
        },
        { 'sender' : 'definitely_not_mike',
          'message' : 'Goodbye world!',
          'timestamp' : datetime.datetime.now()
        },
    ]
    # message['sender']

    # STEP 2: render that information to HTML
    username = request.cookies.get('username')
    return render_template(
            'index.html',
            messages=messages,
            #user='mike izbicki'
            user=username
            )

@app.route('/logout')
def logout():
    res = make_response(render_template(
            'index.html'
            ))
    res.set_cookie('username','',expires=0)
    return res


# http://localhost:5000/login?username=Test&password=Test
# http://localhost:5000/login
@app.route('/login', methods=['GET','POST'])
def login():
    # keys = usernames, values = passwords
    login_credentials={
        'Trump':'12345',
        'Sanders':'password'
    }
    if request.cookies.get('username') is not None:
        return 'You are logged in as: '+request.cookies.get('username')

    # request.args.get = get method
    # request.form.get = post method
    username=request.form.get('user')
    password=request.form.get('password')
    if username in login_credentials and \
        login_credentials[username]== password:
        #return render_template(
        #    'login.html',
        #    successful=True
        #    )
        res = make_response(render_template(
                'login.html',
                successful=True
                ))
        res.set_cookie('username',username)
        return res
    else:
        # access directly
        if username is None and password is None:
            return render_template(
                'login.html'
                )

        # bad user/pass
        else:
            return render_template(
                'login.html',
                bad_userpass=True
                )

@app.route('/static/<path:path>')
def style(path):
    return send_from_directory('static',path)

@app.route('/goodbye')
def goodbye():
    return 'goodbye world'

# /https://google.com
@app.route('/https://<path:url>')
def url(url):
    import requests
    #param=request.args.get('param','')
    #return url
    r=requests.get('https://'+url)
    return r.text

@app.errorhandler(404)
def not_found(e):
    return '404: NOT FOUND.'

# 200 - everything worked
# 404 - file not found
# 500 - internal server error


