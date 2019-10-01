
def filter_odd(lst):
    '''
    return list with odd elements removed
    '''
    result=[]
    for item in lst:
        if item%2==0:
            result.append(item)
    return result



cats=['garfield','kitty','mittens','hobbes']
dogs=['spot','lassie','shenzie']

# colons create slices
# slices return lists
# single indices return single values

pets1=cats+dogs
pets2=dogs+cats

# numbers a+b = b+a
# not true for lists, lists are not commutative

pets=[]
pets+=cats
pets+=dogs

pets3=[]
pets3.extend(cats)
pets3.extend(dogs)

# nested lists
nested_pets=[cats,dogs]

dogs.append('chester')
dogs.extend(['chester'])

pets_chester=[]
pets_chester+=cats
pets_chester+=dogs

pets.remove('garfield')
pets_chester.remove('chester')
del pets

