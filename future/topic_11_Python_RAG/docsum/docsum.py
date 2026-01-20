

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

def split_text(text, max_chunk_size=1000):
    '''
    Takes a string as input and returns a list of strings
    that are all smaller than max_chunk_size.

    >>> split_text('abcdefg', max_chunk_size=2)
    ['ab', 'cd', 'ef', 'g']
    >>> split_text('this is an example', max_chunk_size=3)
    ['thi', ' is', ' an', ' ex', 'amp', 'le']

    This is the simplest possible way to split text.
    Much more sophisticated possibilities.
    Other more complex algorithms will:
    1) try not to split words/sentences/paragraphs
    2) provide overlaps between the chunks
    '''
    accumulator = []
    while len(text) > 0:
        accumulator.append(text[:max_chunk_size])
        text = text[max_chunk_size:]
    return accumulator

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
    try:
        output = llm(prompt)
        return output.split('\n')[-1]
    except groq.APIStatusError:
        chunks = split_text(text, 10000)
        print('len(chunks)=', len(chunks))
        accumulator = []
        for i, chunk in enumerate(chunks):
            print('i=', i)
            # recursion is when you call a function inside itself
            summary = summarize_text(chunk)
            accumulator.append(summary)
        summarized_text = ' '.join(accumulator)
        summarized_text = summarize_text(summarized_text)
        # print('summarized_text=', summarized_text)
        return summarized_text

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        prog='docsum',
        description='summarize the input document',
        )
    parser.add_argument('filename')
    args = parser.parse_args()

    from dotenv import load_dotenv
    load_dotenv()

    import os
    from groq import Groq
    import groq

    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),  # This is the default and can be omitted
    )
    # one way to solve the problem of too much text for the context window
    # is to remove the "unnecessary" text;
    # for html files, that is the html tags
    from bs4 import BeautifulSoup
    with open(args.filename, 'r') as fin:
        html = fin.read()
        soup = BeautifulSoup(html, features="lxml")
        text = soup.text
        #print('text=', text)
        print(summarize_text(text))