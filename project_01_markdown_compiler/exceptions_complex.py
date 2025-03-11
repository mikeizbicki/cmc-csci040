grades={
    'alice':{'hw1':99,'hw2':88},
    'bob':{'hw1':82,'hw2':91},
    'charlie': {'hw2': 90}
    }
#sorted(grades.items())
for k,v in sorted(grades.items()):
    #print(k)
    print(v['hw1'])
