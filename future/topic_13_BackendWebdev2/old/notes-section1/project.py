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
    # request is different from request*s*

    # these variables are set by the information after the ? in the URL;
    # args = arguments; the information after the ? is called the query arguments;
    # these variables are just for 1 webpage
    print("request.args.get('username')=",request.args.get('username'))
    print("request.args.get('password')=",request.args.get('password'))

    # this information comes from a POST form,
    # the methods for the route must include 'POST';
    # these variables are just for 1 webpage
    print("request.form.get('username')=",request.form.get('username'))
    print("request.form.get('password')=",request.form.get('password'))

    # these variables pass between different webpages;
    # these are "persistent"; the other variables are "effemeral"
    print("request.cookies.get('username')=",request.cookies.get('username'))
    print("request.cookies.get('password')=",request.cookies.get('password'))


def is_valid_login(con, username, password):
    '''
    Return True if the given username/password is a valid login;
    otherwise return False.
    '''

    # query the database for users with the given username/password
    
    # when someone is able to enter SQL into the variables (username/password)
    # and change the behavior of the SQL statement, that's SQL injection
    '''
    sql = """
    SELECT username,password
    FROM users
    WHERE username='"""+str(username).replace("'", "''")+"""'
      AND password='"""+str(password)+"""';
    """
    print('is_valid_login: sql=',sql)
    # .replace("'", "''") strategy is not enough to protect you from sql injection
    cur = con.cursor()
    cur.execute(sql)
    '''
    sql = """
    SELECT username,password
    FROM users
    WHERE username=?  
      AND password=?;
    """
    # ? means we don't know the value, but it'll come later
    cur = con.cursor()
    parameters = [username, password]
    cur.execute(sql, parameters) # this is where we specify what the ? are equal to
    rows = cur.fetchall()
    '''
    SELECT username,password
    FROM users
    WHERE (username='Trump'
      AND password='') OR ''='';
    '''
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

    # modify the behavior of this route depending on whether the user is logged in

    username = request.cookies.get('username')
    password = request.cookies.get('password')
    is_logged_in = is_valid_login(con, username, password)

    return render_template('root.html', is_logged_in=is_logged_in)


@app.route('/login', methods=['GET','POST'])
def login():
    con = sqlite3.connect(args.db_file)
    print_debug_info()

    # the basic idea:
    # we will get the information from the POST request;
    # if it's correct, set some cookies;
    # we can always check using cookies to determine whether someone is logged in or not
    form_username = request.form.get('username')
    form_password = request.form.get('password')
    print('form_username=', form_username)
    print('form_password=', form_password)

    has_clicked_form = form_username is not None
    print('has_clicked_form=', has_clicked_form)

    if has_clicked_form:
        login_info_correct = is_valid_login(con, form_username, form_password)
        if login_info_correct:
            # if someone has clicked on the form;
            # and the form information is correct;
            # then we should set the cookies
            response = make_response(render_template('login.html'))
            response.set_cookie('username', form_username)
            response.set_cookie('password', form_password)
            return response

        else:
            # if someone has clicked on the form;
            # and the form information is wrong;
            # then we should display an error
            return render_template('login.html', display_error=True)

    else:
        # if someone has not clicked on the form;
        # do nothing special
        return render_template('login.html')
    

@app.route('/logout')     
def logout():
    print_debug_info()
    #return render_template('logout.html')
    response = make_response(render_template('logout.html'))
    response.set_cookie('username', '', expires=0)
    response.set_cookie('password', '', expires=0)
    return response
    

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
