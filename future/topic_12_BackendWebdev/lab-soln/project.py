########################################
# globals
########################################

from flask import Flask, render_template, send_from_directory
app = Flask(__name__)

# sqlite3 is built in python3, no need to pip3 install
import sqlite3

# process command line arguments
import argparse
parser = argparse.ArgumentParser(description='Create a database for the twitter project')
parser.add_argument('--db_file', default='twitter_clone.db')
args = parser.parse_args()


########################################
# routes
########################################

@app.route('/')     
def root():
    # connect to the database
    con = sqlite3.connect(args.db_file)

    # construct messages,
    # which is a list of dictionaries,
    # where each dictionary contains the information about a message
    messages = []
    sql = 'select sender_id,message,created_at from messages order by created_at desc;'
    cur_messages = con.cursor()
    cur_messages.execute(sql)
    for row_messages in cur_messages.fetchall():

        # get the username/age from sender_id
        sql='select username,age from users where id='+str(row_messages[0])+';'
        cur_users = con.cursor()
        cur_users.execute(sql)
        for row_users in cur_users.fetchall():
            pass

        # build the message dictionary
        messages.append({
            'message': row_messages[1],
            'created_at': row_messages[2],
            'username': row_users[0],
            'age': row_users[1]
            })

    # render the jinja2 template and pass the result to firefox
    return render_template('root.html', messages=messages)


@app.route('/login')     
def login():
    return render_template('login.html')
    

@app.route('/logout')     
def logout():
    return render_template('logout.html')
    

@app.route('/create_message')     
def create_message():
    return render_template('create_message.html')
    

@app.route('/create_user')     
def create_user():
    return render_template('create_user.html')
    

@app.route('/static/<path>')
def static_directory(path):
        return send_from_directory('static',path)


########################################
# boilerplate
########################################

app.run()
