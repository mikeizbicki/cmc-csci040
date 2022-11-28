'''
This is a "hello world" flask webpage.

NOTE:
the module flask is not built-in to python,
so you must run pip install in order to get it.
After doing do, this file should "just work".
'''

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')     
def root():
    return "hello world"

app.run()
