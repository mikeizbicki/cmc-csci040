# pip install flask for this to work
from flask import Flask, render_template
app = Flask(__name__)

# any time you see @ that's called a "decorator"
@app.route('/')     
def root():
    return 'hello <b>world</b>'

@app.route('/users') 
def users():
    username = 'Mike'*1000
    
    users = ['mike', 'kristen', 'evan', 'issac']

    return render_template('users.html', username=username, users=users)

app.run()