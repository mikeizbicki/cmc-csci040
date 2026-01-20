# these are the term counts calculated in the lab
lab_dict = {
    'russia': 412,
    'trump': 13924,
    'obama': 2712,
    'mexico': 199,
    }

terms = list(lab_dict.keys())
print(f'terms={terms}')

counts = list(lab_dict.values())
print(f'counts={counts}')

sorted_terms = []
sorted_counts = []
for i, term in enumerate(sorted(terms)):
    sorted_terms.append(term)
    sorted_counts.append(lab_dict[term])

print(f'sorted_terms={sorted_terms}')
print(f'sorted_counts={sorted_counts}')


# this code generates a plot
import matplotlib.pyplot as plt
plt.bar(sorted_terms, sorted_counts)
plt.show()
#plt.savefig('my_figure.png')
