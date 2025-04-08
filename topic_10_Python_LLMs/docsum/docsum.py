import argparse
parser = argparse.ArgumentParser(
    prog='docsum',
    description='summarize the input document',
    )
parser.add_argument('filename')
args = parser.parse_args()
#print('filename=', args.filename)

with open(args.filename, 'r') as fin:
    text = fin.read()
#print('text=', text)

from dotenv import load_dotenv
load_dotenv()

import os
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),  # This is the default and can be omitted
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            # content = prompt
            # Any time I'm using an LLM,
            # I always provide an instruction about how long
            # the output should be
            "content": f"Summarize the following document in 1 paragraph (max 3 sentences): {text}",
        }
    ],
    model="llama3-8b-8192",
)
print(chat_completion.choices[0].message.content)