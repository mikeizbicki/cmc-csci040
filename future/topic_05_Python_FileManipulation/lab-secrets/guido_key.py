from zipfile import ZipFile
import zlib

with open('Ashley-Madison.txt', encoding='ascii') as f:
    passwords = f.read().split('\n')

for i,password in enumerate(passwords):
    if i%1000==0:
        print('i=',i,'password=',password)
    with ZipFile('whitehouse_secrets.zip') as zf:
        try:
            zf.extractall(pwd=password.encode('ascii'))
            print('password=', password)
            break
        except (RuntimeError, zlib.error):
            pass


