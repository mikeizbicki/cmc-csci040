# pip install flask for this to work
from flask import Flask, render_template
app = Flask(__name__)

# any time you see @ that's called a "decorator"
@app.route('/')     
def root():
    message = 'hello world'*100
    return message

@app.route('/users')
def users():
    users = ['Mike', 'Kristen', 'Evan', 'Isaac', 'Trump', 'Biden']
    # my recommendation for the messages is to use a list of dictionaries
    for user in users:
        print('user=',user)
    return render_template('users.html', username='Kristen', users=users)
    # render_template looks in your PWD/templates/ for the files you specify

app.run()