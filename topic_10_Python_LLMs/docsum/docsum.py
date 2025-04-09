import argparse
parser = argparse.ArgumentParser(
    prog='docsum',
    description='summarize the input document',
    )
parser.add_argument('filename')
args = parser.parse_args()
#print('filename=', args.filename)


from dotenv import load_dotenv
load_dotenv()

import os
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),  # This is the default and can be omitted
)

def llm(text):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                # content = prompt
                # Any time I'm using an LLM,
                # I always provide an instruction about how long
                # the output should be
                "content": text,
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content

def summarize_text(text):
    '''
    Our current problem: we cannot summarize large documents.
    Our solution: recusive summarization.
    Other solutions exist, no one nows what the best one is.
    We use recursive sum. because it is easy and illustrates good CS concepts.

    Two step process:
    1) Split the document into chunks that are the size of the context window.
       Summarize those chunks using the LLM.
       This gives us a sequence of smaller documents that we will append together to 
        create a new document that contains the same information as the original doc
        but is smaller.
    2) Call summarize_text on this new smaller document.
    '''
    prompt = f'''
    Summarize the following text in 1-3 sentences.

    {text}
    '''
    output = llm(prompt)
    return output.split('\n')[-1]

#import requests
#requests.get(args.filename)

# why error on docs/news-mx.html?
# every LLM has a "context window size" which is the number of
# "tokens" it is able to view at once;
# "token" is a part of a word; roughly 1 word = 2 tokens on average
# the context window size of the default groq model (llama3-8b-8192)
# is 8192 tokens;
# this is the largest document we can pass in to the model;
# roughly means ~4000 words;
# what we need to do to get our program to work on html is:
# strip the contents of the html file of all the html tags;
# get the raw text from the html
'''
with open(args.filename, 'r') as fin:
    text = fin.read()
    print(summarize_text(text))
'''

'''
import fulltext
text = fulltext.get(args.filename, None)
print('text=', text)
#print(summarize_text(text))
'''

# one way to solve the problem of too much text for the context window
# is to remove the "unnecessary" text;
# for html files, that is the html tags
from bs4 import BeautifulSoup
with open(args.filename, 'r') as fin:
    html = fin.read()
    soup = BeautifulSoup(html)
    text = soup.text
    #print('text=', text)
    print(summarize_text(text))