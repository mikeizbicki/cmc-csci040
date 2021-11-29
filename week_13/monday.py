# pip install flask for this to work
from flask import Flask
app = Flask(__name__)

@app.route('/')
def root():
    return 'hello <b>world</b>'

app.run()