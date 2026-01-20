# these are the term counts calculated in the lab
lab_dict = {
    'russia': 412,
    'trump': 13924,
    'obama': 2712,
    'mexico': 199,
    }

terms = lab_dict.keys()
print(f'terms={terms}')

counts = lab_dict.values()
print(f'counts={counts}')

# this code generates a plot
import matplotlib.pyplot as plt
plt.bar(terms, counts)
plt.show()
