# boilerplate code
# Django popular python web framework, requires dozens of lines of code and many files
from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

@app.route('/')
def root():
    #return 'hello <b>world</b>'
    return render_template('index.html')
    #return render_template('templates/index.html') this is incorrect

@app.route('/twitter') # no colon on this line; decorator
def twitter():
    return 'this is twitter'

'''
@app.route('/user/mike')
def twitter():
    return 'this is mike'

@app.route('/user/trump')
def twitter():
    return 'this is trump'

@app.route('/user/biden')
def twitter():
    return 'this is biden'
'''

@app.route('/user/<username>') # flask only syntax
def user(username):
    #return 'this is '+username
    return render_template(
        'user.html',
        username=username
        )
        # flask uses the jinja2 templating language in order to substitute variables

@app.route('/https://<url>')
def url(url):
    import requests
    r = requests.get('https://'+url)
    return r.text

@app.route('/sentiment/<sentence>')
def sentiment(sentence):
    from textblob import TextBlob
    blob = TextBlob(sentence)
    polarity = blob.polarity
    subjectivity = blob.subjectivity
    return '{ "polarity":'+str(polarity) + ', "subjectivity": '+str(subjectivity)+'}'

@app.errorhandler(404)
def error_message(e):
    return '404: NOT FOUND'

@app.route('/static/<path>')
def static_directory(path):
    return send_from_directory('static',path)

app.run()