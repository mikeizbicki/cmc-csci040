1+2
'hello world'
print(1+2)
print('hello world')

print('enter your name: ')
name=input()
print('your name is '+name)
print('your name has '+str(len(name))+' characters')

if len(name) > 5:
    print('you might have a long name')
    
if len(name) > 10:
    print('you do have a long name')
elif len(name) < 5:
    print('you have a short name')
else:
    print('you have a medium name')
    
#if len(name) < 5:
#    print('you have a short name')
#if len(name) >=5 and len(name) <= 10:
#    print('you have a medium name')
