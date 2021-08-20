import sqlite3
from flask import Flask, render_template, send_from_directory, request, make_response
app = Flask(__name__)

def is_logged_in(cur, username, password):
    sql = '''
        SELECT username,password FROM users where username=? and password=?;
    '''
    #sql = '''
    #    SELECT username,password FROM users where username='''+username+' and '+'pasword='+password+'''
    #'''
    cur.execute(sql, (username,password,))
    rows = cur.fetchall()

    if len(list(rows))==0:
        return False
    else:
        return True

@app.route('/.json')
def root_json():
    messages = [
        { 'text' : "I'm a baby", 'username':'Evan'},
        { 'text' : "I'm a baby", 'username':'Biden'},
        { 'text' : "I'm a baby", 'username':'Trump'},
    ]
    return json.dumps(messages)

@app.route('/')
def root():

    # generate a list of messages manually for debugging
    messages = [
        { 'text' : "I'm a baby", 'username':'Evan'},
        { 'text' : "I'm a baby", 'username':'Biden'},
        { 'text' : "I'm a baby", 'username':'Trump'},
    ]

    # generate a list of messages from the db
    con = sqlite3.connect('twitter_clone.db')
    cur = con.cursor()
    sql = '''
        SELECT sender_id,message,id FROM messages;
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
            'username' : username,
            'id' : row[2]
        })

    # render the webpage
    #logged_in=True
    #username=request.cookies.get('username')
    #if logged_in:

    #logged_in = request.cookies.get('username')
    # check whether the username/password is correct in the db
    con = sqlite3.connect('twitter_clone.db')
    cur = con.cursor()
    
    login_successful = is_logged_in(
        cur=cur,
        username=request.cookies.get('username'),
        password=request.cookies.get('password'),
    )

    if login_successful:
        return render_template(
            'root.html',
            username=request.cookies.get('username'),
            messages=messages
            )
    else:
        return render_template(
            'root.html',
            messages=messages
            )


@app.route('/login', methods=['get','post'])
def login():
    #if request.args.get('username'):
    if request.form.get('username'):
        
        # check whether the username/password is correct in the db
        
        con = sqlite3.connect('twitter_clone.db')
        cur = con.cursor()
        login_successful = is_logged_in(
            cur=cur,
            username=request.form.get('username'),
            password=request.form.get('password'),
        )
        """
        sql = '''
            SELECT username,password FROM users where username=? and password=?;
        '''
        cur.execute(sql, (request.form.get('username'), request.form.get('password')))
        rows = cur.fetchall()

        if len(list(rows))==0:
            login_successful=False
        else:
            login_successful=True
            """


        # check the database to see if their login credentials are correct
        #username = 'mike'
        #password = '12345'
        #if request.args.get('username')==username and request.args.get('password')==password:  
        #if request.form.get('username')==username and request.form.get('password')==password:  
        if login_successful:
            # set the cookie value
            res = make_response(render_template(
                'login.html',
                login_successful=True,
                username=request.form.get('username')
                ))
            #res.set_cookie('username',request.args.get('username'))
            res.set_cookie('username',request.form.get('username'))
            res.set_cookie('password',request.form.get('password'))
            return res
        else:
            return render_template(
                'login.html',
                login_unsuccessful=True
                )
    else:
        return render_template(
                'login.html',
                login_default=True
                )


@app.route('/logout')
def logout():
    res = make_response(render_template(
        'logout.html',
        ))
    res.set_cookie('username','',expires=0)
    res.set_cookie('password','',expires=0)
    return res

@app.route('/delete_message/<id>')
def delete_message(id):
    con = sqlite3.connect('twitter_clone.db')
    cur = con.cursor()
    if is_logged_in(
        cur=cur,
        username=request.cookies.get('username'),
        password=request.cookies.get('password'),
    ):
        # get username from the cookies
        sql='''
        DELETE FROM messages WHERE id=?;
        '''
        cur.execute(sql, (id,))
        con.commit()
    return 'message deleted'


@app.route('/delete_user')
def delete_user():
    # get username from the cookies
    sql='''
    DELETE FROM users WHERE username=?;
    '''
    cur.execute(sql, (username,))
    con.commit()

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
