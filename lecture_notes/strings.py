words={
    'hte':'the',
    'Hte':'The',
    'hTe':'The',
    'HTE':'The',
    'claremont':'Claremont',
    }

def spell_check(s):
    tokens=s.split(' ')
    tokens_modified=[]
    for token in tokens:
        if token in words.keys():
            tokens_modified.append(words[token])
            print('found ',token)
        else:
            tokens_modified.append(token)
    print('tokens=',tokens)
    print('tokens_modified=',tokens_modified)
    s_corrected=' '.join(tokens_modified)
    return s_corrected

corrected=spell_check('this class is hte best!')
print('corrected=',corrected)
