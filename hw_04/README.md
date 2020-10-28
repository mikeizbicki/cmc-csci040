# HW 4: Scraping from ebay

![comic](D1Kq7tHUYAA4CKC.jpeg)

**Description:** 
You will scrape information from ebay and store the results in a json file.

**Due:** 
Sunday, 8 November, midnight

**Learning objectives:**

1. understand how web scraping works
1. complete a python project entirely on your own (no starter code!)
1. integrate python knowledge with HTML knowledge

## Instructions

Write a python script that:

1. Uses the requests library to download the first 10 webpage results for a search term of your choice

2. Uses bs4 to extract all of the items returned in the search results

3. Creates a python list of the extracted items, where each entry in the list is a dictionary.
   The dictionary should have three keys:

   1. `name` will contain the name of the item
   2. `price` will contain the price of the item
   3. `status` will contain a string stating whether the item is "Brand New", "Refurbished", "Pre-owned", etc.

4. Uses the json library to save the list as a json file named `items.json`

Create a github repo that:

1. Contains your python file

1. Contains your `items.json` file

1. Contains a `README.md` file explaining:

    1. what your search term is

Submit your assignment by uploading a link to the github repo to sakai

## Grading rubric

3 pts: use of the requests library to download the webpage

3 pts: use of bs4 to extract the items from the webpage

3 pts: outputting a json file

6 pts: extracting items from all pages in the search results
