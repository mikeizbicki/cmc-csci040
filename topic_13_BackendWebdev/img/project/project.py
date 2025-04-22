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

from flask import Flask, render_template, request, make_response
app = Flask(__name__)

# anything that starts with a @ is called a "decorator" in python
# in general, decorators modify the functions that follow them
@app.route('/')     
def root():
    print_debug_info()
    '''
    text = 'hello cs40'
    text = '<strong>' + text + '</strong>' # + 100
    return text
    '''
    messages = [{}]

    # check if logged in correctly
    username = request.cookies.get('username')
    password = request.cookies.get('password')
    good_credentials = are_credentials_good(username, password)
    print('good_credentials=', good_credentials)

    # render_template does preprocessing of the input html file;
    # technically, the input to the render_template function is in a language called jinja2
    # the output of render_template is html
    return render_template('root.html', logged_in=good_credentials, messages=messages)


def print_debug_info():
    # GET method
    print('request.args.get("username")=', request.args.get("username"))
    print('request.args.get("password")=', request.args.get("password"))

    # POST method
    print('request.form.get("username")=', request.form.get("username"))
    print('request.form.get("password")=', request.form.get("password"))

    # cookies
    print('request.cookies.get("username")=', request.cookies.get("username"))
    print('request.cookies.get("password")=', request.cookies.get("password"))


def are_credentials_good(username, password):
    # FIXME:
    # look inside the databasse and check if the password is correct for the user
    if username == 'haxor' and password == '1337':
        return True
    else:
        return False


@app.route('/login', methods=['GET', 'POST'])     
def login():
    print_debug_info()
    # requests (plural) library for downloading;
    # now we need request singular 
    username = request.form.get('username')
    password = request.form.get('password')
    print('username=', username)
    print('password=', password)

    good_credentials = are_credentials_good(username, password)
    print('good_credentials=', good_credentials)

    # the first time we've visited, no form submission
    if username is None:
        return render_template('login.html', bad_credentials=False)

    # they submitted a form; we're on the POST method
    else:
        if not good_credentials:
            return render_template('login.html', bad_credentials=True)
        else:
            # if we get here, then we're logged in
            #return 'login successful'

            # create a cookie that contains the username/password info

            template = render_template(
                'login.html', 
                bad_credentials=False,
                logged_in=True)
            #return template
            response = make_response(template)
            response.set_cookie('username', username)
            response.set_cookie('password', password)
            return response

# scheme://hostname/path
# the @app.route defines the path
# the hostname and scheme are given to you in the output of the triangle button
# for settings, the url is http://127.0.0.1:5000/logout to get this route
@app.route('/logout')     
def logout():
    print_debug_info()
    #1 + 'error' # this will throw an error
    return 'logout page'

# 403 error code


app.run()
