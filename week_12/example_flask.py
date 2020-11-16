#from app import app
from flask import Flask, request, render_template, send_from_directory, make_response
app = Flask(__name__)
import sqlite3
import datetime

# decorator
@app.route('/')
def root():
    return 'hello world'
    return render_template(
            'index.html',
            #messages=messages,
            username=request.cookies.get('username'),
            )

@app.route('/logout', methods=['GET'])
def logout():
    res = make_response(render_template(
            'logout.html'
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

if __name__ == '__main__':
    app.run(debug = True)
