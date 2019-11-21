from app import app

from flask import request

# decorator
@app.route('/hello')
def hello():
    return 'hello world'

@app.route('/goodbye')
def goodbye():
    return 'goodbye world'

# /url?param=https://google.com
@app.route('/url')
def url():
    import requests
    param=request.args.get('param','')
    r=requests.get(param)
    return r.text

@app.errorhandler(404)
def not_found(e):
    return '404: NOT FOUND.'
