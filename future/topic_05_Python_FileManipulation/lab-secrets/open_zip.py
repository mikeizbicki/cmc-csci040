from zipfile import ZipFile

with ZipFile('guido_secrets.zip') as zf:
    zf.extractall(pwd='1956-01-31'.encode('ascii'))
