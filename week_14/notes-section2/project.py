########################################
# flask/db setup
########################################

from flask import Flask, render_template, request, make_response
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

    # this code below uses request (singular) different from requests (plural) that we've seen before

    # HTML Form GET
    # these values here are called "query arguments" (args is an abreviation);
    # they are the values after the ? in the url;
    # they 1 one webpage only
    print("request.args.get('username')=",request.args.get('username'))
    print("request.args.get('password')=",request.args.get('password'))

    # HTML Form POST
    # method=POST on the html form in the html;
    # the variables not included in the url, so it's good for passwords;
    # this will only affect 1 webpage
    print("request.form.get('username')=",request.form.get('username'))
    print("request.form.get('password')=",request.form.get('password'))

    # Cookies
    # not visible to the user directly (not in the url)
    # they persist on every webpage you visit
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
    con = sqlite3.connect(args.db_file)
    print_debug_info()

    # this code will check whether we are logged in or not
    # idea:
    # get the username/password from the cookies
    # check if the username/password exists in the database
    username = request.cookies.get('username')
    password = request.cookies.get('password')

    is_logged_in = is_valid_login(con, username, password)
    print('is_logged_in=',is_logged_in)

    return render_template('root.html', is_logged_in=is_logged_in)

# the default is:
# @app.route('/login', methods=['GET'])
@app.route('/login', methods=['GET','POST'])
def login():
    con = sqlite3.connect(args.db_file)
    print_debug_info()

    # if the user has submitted something from a form
    # check to see if the submission is a valid login
    # if it is, we'll set the appropriate cookies
    # if it is not, we'll display an error (not set the cookies)

    form_username = request.form.get('username')
    form_password = request.form.get('password')
    print('form_username=',form_username)
    print('form_password=',form_password)

    has_used_form = form_username is not None
    print('has_used_form=',has_used_form)

    if has_used_form:
        valid_login = is_valid_login(con, form_username, form_password)
        if valid_login:
            # successful login
            result = make_response(render_template('login.html', successful_login=True))
            result.set_cookie('username', form_username)
            result.set_cookie('password', form_password)
            return result
        else:
            # unsuccessful login
            return render_template('login.html', unsuccessful_login=True)
    else:
        # they haven't tried to login yet
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
