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

from flask import Flask, render_template
app = Flask(__name__)

# anything that starts with a @ is called a "decorator" in python
# in general, decorators modify the functions that follow them
@app.route('/')     
def root():
    '''
    text = 'hello cs40'
    text = '<strong>' + text + '</strong>' # + 100
    return text
    '''
    # render_template does preprocessing of the input html file;
    # technically, the input to the render_template function is in a language called jinja2
    # the output of render_template is html
    return render_template('root.html')

@app.route('/login')     
def login():
    return render_template('login.html')

# scheme://hostname/path
# the @app.route defines the path
# the hostname and scheme are given to you in the output of the triangle button
# for settings, the url is http://127.0.0.1:5000/logout to get this route
@app.route('/logout')     
def logout():
    1 + 'error' # this will throw an error
    return 'logout page'

# 403 error code


app.run()
