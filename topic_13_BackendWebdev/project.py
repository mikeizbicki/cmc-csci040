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

from flask import Flask
app = Flask(__name__)

# Anything that starts with a @ is called a "decorator" in python.
# Decorators modify the functions that follow them.
# The flask library uses decorators to convert functions into *routes*.
# A route is a *path* that is visible in the web server.
@app.route('/')
def root():
    text = 'hello <strong>cs40</strong>'
    return text

@app.route('/example')
def example():
    text = 'example'
    return text

app.run()
