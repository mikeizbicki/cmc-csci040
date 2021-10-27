# HW 4: Scraping from ebay

![comic](D1Kq7tHUYAA4CKC.jpeg)

**Description:** 
You will scrape information from ebay and store the results in a json file.

**Due:** 
Sunday, 7 November, midnight

**Learning objectives:**

1. understand how web scraping works
1. complete a python project entirely on your own (no starter code!)
1. integrate python knowledge with HTML knowledge+JSON knowledge

## Instructions

**PART I:**

Create a python file names `ebay-dl.py`.
Your file should:

1. Use the `argparse` library to get a search term from the command line.

1. Use the `requests` library to download the first 10 webpage results for your search term

1. Use `bs4` to extract all of the items returned in the search results

1. Create a python list of the extracted items,
   where each entry in the list is a dictionary.
   The dictionary should have the following keys:
   1. `name` will contain the name of the item
   2. `price` will contain the price of the item in cents, stored as an integer (you should never use floats to store monetary values, because floats can't be represented exactly in computers); if there are multiple prices listed (e.g. `$54.99 to $79.99`), then you may select either price
   3. `status` will contain a string stating whether the item is "Brand New", "Refurbished", "Pre-owned", etc.
   4. `shipping` will contain the price of shipping the item in cents, stored as an integer; if the item has free shipping, then this value should be `0`
   5. `free_returns` will contain a boolean value for whether the item has free returns
   6. `items_sold` will contain the number of items sold (as an integer)
   
   **NOTE:**
   Not every item listed on ebay will have an entry for each of the fields in the dictionary above.
   If there is no entry, then your dictionary must still have the associated key, and the value should be `None`.

1. Use the `json` library to save the list as a json file named `SEARCH_TERM.json`, where `SEARCH_TERM` should be replaced by the search term passed in on the command line.

**PART II:**

Run your `ebay-dl.py` file on 3 search terms of your choice,
generating 3 different json files.
At least one of these search terms must contain a space (e.g. `drill press`, `stuffed animal`, or `claremont mckenna`).

**PART III:**

Create a github repo that:

1. Contains your `ebay-dl.py` file

1. Contains your 3 json files

1. Contains a `README.md` file explaining:

    1. what your `ebay-dl.py` file does

    1. how to run your `ebay-dl.py` file, using markdown code block(s) (and not inline code annotations) to show the exact commands that should be run to generate the 3 json files in your repo

    1. a link to the course project

**Submission:**

Submit your assignment by uploading a link to the github repo to sakai

## Grading rubric

The assignment is worth 18 points total.

3 pts: use of the `argparse` library to pass information from the command line

3 pts: use of the requests library to download the webpage

3 pts: use of bs4 to extract the items from the webpage

3 pts: outputting a json file

6 pts: extracting items from all pages in the search results
