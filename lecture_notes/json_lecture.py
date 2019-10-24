import json
with open('JEOPARDY_QUESTIONS1.json','r') as f:
    text=f.read()
    jeopardy=json.loads(text)

count=0
for question in jeopardy:
    category=question['category']
    if category=='HISTORY':
        count+=1
print('count=',count)
print('fraction=',count/len(jeopardy))

#json.loads str -> dict
#json.dumps dict -> str

# What is JSON?
# file format for exchanging data

grades=[{
    'einstein':[90,80,90],
    "izbicki":[100,90,80],
},
{ 'robert frost': [30,40,50],
  'dorthy day': [60,70,80]
}
]

result=json.dumps(grades)
grades2=json.loads(result)

