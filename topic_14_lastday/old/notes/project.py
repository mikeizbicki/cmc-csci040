########################################
# flask/db setup
########################################

from flask import Flask, render_template, request
app = Flask(__name__)

# sqlite3 is built in python3, no need to pip3 install
import sqlite3

# process command line arguments
import argparse
parser = argparse.ArgumentParser(description='Create a database for the twitter project')
parser.add_argument('--db_file', default='twitter_clone.db')
args = parser.parse_args()

########################################
# helper functions
########################################

def print_debug_info():
    '''
    Print information stored in GET/POST/Cookie variables to the terminal.
    '''
    print("request.args.get('username')=",request.args.get('username'))
    print("request.args.get('password')=",request.args.get('password'))
    print("request.form.get('username')=",request.form.get('username'))
    print("request.form.get('password')=",request.form.get('password'))
    print("request.cookies.get('username')=",request.cookies.get('username'))
    print("request.cookies.get('password')=",request.cookies.get('password'))


def is_valid_login(con, username, password):
    '''
    Return True if the given username/password is a valid login;
    otherwise return False.
    '''

    # query the database for users with the given username/password
    sql = """
    SELECT username,password
    FROM users
    WHERE username='"""+str(username)+"""'
      AND password='"""+str(password)+"""';
    """
    print('is_valid_login: sql=',sql)
    cur = con.cursor()
    cur.execute(sql)
    rows = cur.fetchall()

    # if the total number of rows returned is 0,
    # then no username/password combo was not found
    if len(list(rows))==0:
        return False

    # if the total number of rows returned is > 0,
    # then the username/password combo was found
    else:
        return True


########################################
# custom routes
########################################

@app.route('/')     
def root():
    print_debug_info()
    return render_template('root.html')


@app.route('/login')
def login():
    print_debug_info()
    return render_template('login.html')
    

@app.route('/logout')     
def logout():
    print_debug_info()
    return render_template('logout.html')
    

@app.route('/create_message')     
def create_message():
    print_debug_info()
    return render_template('create_message.html')
    

@app.route('/create_user')     
def create_user():
    print_debug_info()
    return render_template('create_user.html')
    

########################################
# boilerplate
########################################

if __name__=='__main__':
    app.run()
