patterns=[
    '<NOUN> is a <ADJECTIVE> <NOUN2>!',
    '<NOUN> is a <NOUN2>.'
    ]
pattern='<NOUN> is a <ADJECTIVE> <NOUN2>!'
noun=['Bernie Sanders','snders','Bernie','Sanders']
adjective=['tall','small','crazy','sell-out']
noun2=['politician','leader']

result=pattern.replace('<NOUN>',noun[0])
result=result.replace('<ADJECTIVE>',adjective[0])
result=result.replace('<NOUN2>',noun2[0])
print('result=',result)

import random
print('choice=',random.choice(noun))

for i in range(100):
    pattern=random.choice(patterns)
    result=pattern.replace('<NOUN>',random.choice(noun))
    result=result.replace('<ADJECTIVE>',random.choice(adjective))
    result=result.replace('<NOUN2>',random.choice(noun2))
    print('result=',result)
