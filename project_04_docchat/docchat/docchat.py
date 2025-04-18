import readline
import groq

from dotenv import load_dotenv
load_dotenv()


client = groq.Groq()

def llm(messages, temperature=1):
    '''
    >>> llm([
    ...     {'role': 'system', 'content': 'You are a helpful assistant.'},
    ...     {'role': 'user', 'content': 'What is the capital of France?'},
    ...     ], temperature=0)
    'The capital of France is Paris!'
    '''
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama3-8b-8192",
        temperature=temperature,
    )
    return chat_completion.choices[0].message.content


if __name__ == '__main__':
    messages = []
    messages.append({
        'role': 'system',
        'content': 'You are a helpful assistant.  You always speak like a pirate.  You always answer in 1 sentence.'
    })
    while True:
        # get input from the user
        text = input('docchat> ')
        # pass that input to llm
        messages.append({
            'role': 'user',
            'content': text,
        })
        result = llm(messages)
        # FIXME:
        # Add the "assistant" role to the messages list
        # so that the `llm` has access to the whole
        # conversation history and will know what it has previously
        # said and update its response with that info.

        # print the llm's response to the user
        print('result=', result)
        import pprint
        pprint.pprint(messages)
