from app import app

from flask import request, render_template, send_from_directory

# decorator
@app.route('/')
def hello():
    return render_template(
            'index.html',
            #user='mike izbicki'
            )

@app.route('/login')
def login():
    return render_template(
            'login.html'
            )

@app.route('/static/<path:path>')
def style(path):
    return send_from_directory('static',path)

@app.route('/goodbye')
def goodbye():
    return 'goodbye world'

# /https://google.com
@app.route('/https://<path:url>')
def url(url):
    import requests
    #param=request.args.get('param','')
    #return url
    r=requests.get('https://'+url)
    return r.text

@app.errorhandler(404)
def not_found(e):
    return '404: NOT FOUND.'

# 200 - everything worked
# 404 - file not found
# 500 - internal server error


