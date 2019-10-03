print('hello world')

# square bracket [ list
# parenthesis ( tuple
# curly brace { dict

dictionary={
    'key':'this is something you use to unlock doors',
    'door':'a moveable wall',
}

calendar={
    'Monday':'boring',
    'Tuesday':'yay! cs40!!!',
    'Wednesday':'boring',
    'Thursday':'yay! cs40!!!',
    'Friday':'boring',
    'Friday':'exciting :)',
}

# print all boring days
#for key in calendar.keys():
for day in sorted(calendar.keys()):
    if calendar[day]=='boring':
        print('day ',day,'is',calendar[day])


