'''
In this lab, you will practice scraping information from the web
using the requests and bs4 libraries.

Your goal is to:

    1. Use the requests library to search ebay for any type of item

    2. Use bs4 to extract all of the items returned in the search results

    3. Create a python list of the extracted items, where each entry in the 
       list is a dictionary.  The dictionary should have three keys:

       i. the name of the item
       ii. the price of the item
       iii. whether the item is "Brand New", "Refurbished", "Pre-owned", etc.

    4. Use the json library to save the list as a json file named "items.json"

    5. If you complete the steps above for only the first search page, 
       you will get 8/10 points on the lab.  To get the full 10/10 points,
       you need to additionally include all items from the first 10 pages of 
       search results.  (This will require repeating steps 1-3 for 10
       different webpages.)

    6. Upload your lab.py and items.json files to sakai.

HINT: 
Steps 1-3(i,ii) are exactly what we did in lecture.
Step 3(iii) requires you to look at ebay's html for your self to figure 
out how to extract the information.
Step 4 is using the json library, which we covered several lectures ago.
Step 5 requires you to put all the previous steps in a for loop,
and figure out which urls you need to download to get the right information 
from ebay.
'''
