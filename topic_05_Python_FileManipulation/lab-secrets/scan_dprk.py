import ipaddress
import requests
import urllib3

def claremont_ips():
    '''
    https://ipinfo.io/AS3659
    '''

    range1 = [ ipaddress.ip_address('134.173.0.0') + i for i in range(65536) ] 
    return [ str(ip) for ip in range1 ]

def dprk_ips():
    '''
    '''

    range1 = [ ipaddress.ip_address('175.45.176.0') + i for i in range(1024) ] 
    range2 = [ ipaddress.ip_address('210.52.109.0') + i for i in range(256) ]
    return [ str(ip) for ip in range1 + range2 ]


def typo_strings(s):
    '''
    >>> typo_strings('google.com')[:4]
    ['aoogle.com', 'boogle.com', 'coogle.com', 'doogle.com']
    '''
    typos = []
    for i,c in enumerate(s):
        for c2 in 'qwertyuiopasdfghjklzxcvbnm':
            typo = s[:i] + c2 + s[i+1:]
            typos.append(typo)
        if c=='.':
            break
    return typos


hosts = []
total_hosts = 0
for ip in dprk_ips():
    print('ip='+ip)
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'
        }
        requests.get('http://'+ip, headers=headers, timeout=10)
        hosts.append(ip)
        print('  HOST DETECTED!')
        total_hosts += 1
    except (requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError):
        pass

print("total_hosts=",total_hosts)
print("hosts=",hosts)
