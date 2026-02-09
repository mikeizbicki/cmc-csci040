import requests

#ip = '175.45.176.71'
ip = '175.45.176.80'
#ip = 'www.kcna.kp'
headers = {
    #'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
    'Host': 'l33t h4x0r',
}
requests.get('http://'+ip, headers=headers, timeout=10)

