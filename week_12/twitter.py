import sqlite3
from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/home')
def home():
    logged_in=True
    username='mike'

    con = sqlite3.connect('twitter_clone.db')
    cur = con.cursor()
    sql = '''
        SELECT sender_id,message FROM messages;
    '''
    cur.execute(sql)
    rows = cur.fetchall()
    messages = []
    for row in rows:
        sql = '''
            SELECT username FROM users WHERE id=?
        '''
        cur.execute(sql, (row[0],))
        username_rows = cur.fetchall()
        for username_row in username_rows:
            username = username_row[0]
        messages.append({
            'text' : row[1],
            'username' : username #row[0]
        })

    '''
    messages = [
        { 'text' : "I'm a baby", 'username':'Evan'},
        { 'text' : "I'm a baby", 'username':'Biden'},
        { 'text' : "I'm a baby", 'username':'Trump'},
    ]
    '''

    if logged_in:
        return render_template(
            'home.html',
            username=username,
            messages=messages
            )
    else:
        return render_template(
            'home.html',
            messages=messages
            )

@app.route('/user/<username>')
def user(username):
    return render_template(
        'user.html',
        username=username
        )

@app.route('/static/<path>')
def static_directory(path):
    return send_from_directory('static',path)

###############################################################################
# routes below here are examples and not important for the twitter clone
###############################################################################

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


app.run()