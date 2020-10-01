# this is the output of the lab
counts = {'trump': 13924, 'russia': 412, 'obama': 2712, 'fake news': 333, 'mexico': 199}

import matplotlib.pyplot as plt

'''
fig, [ax1, ax2] = plt.subplots(2)
ax1.set(xlabel='these are the words')
ax1.set(ylabel='the number of times Trump tweeted the word')
ax1.bar( counts.keys() , counts.values() )
ax2.bar( [1,2,3], [4,3,2] )
#plt.show()
'''

fig, ax = plt.subplots()
ax.set(
    xlabel='these are the words',
    ylabel='the number of times Trump tweeted the word',
    )
x = list(reversed(sorted(counts.keys())) )
# heights = sorted(counts.values())
heights = []
for label in x:
    heights.append(counts[label])

print('heights=',heights)

ax.bar( x , heights )
plt.show()

# .keys() is non-deterministic
# sorted(counts.keys()) is deterministic
print('counts.keys()=',sorted(counts.keys()))