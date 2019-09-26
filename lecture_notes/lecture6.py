password='p4ssw0rd'
#guess=''

'''
while guess != password:
    print('guess the password:')
    guess=input()
    #Guess=input()
print('guess the password')
'''
while True:
    print('guess the password:')
    guess=input()
    if guess==password:
        break
    for i in range(5):
        print('i=',i)

number=34567
counter=0
while number>0:
    number//=10
    counter+=1
    print('number=',number,'counter=',counter)
    #number=number//10
print('number=',number)

# to escape infinite loop type CTRL+C

total=0
Total=0
# if statement = once; while statement = repeatedly
while total<5:
    total+=1
    print('Total=',Total)
print('total=',total)

total=0
for i in range(5):
    total+=1
print('total=',total)


