import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(w):
    w = w.lower()
    if w in data.keys():
        return data[w]
    elif get_close_matches(w, data.keys()):
        yn = input('There is no this word in dictionary, maybe you want to print:\n{}\nPrint Y for yes or N for no: '.format(get_close_matches(w, data.keys())[0]))
        if yn == 'Y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == 'N':
            return 'There is no this word in dictionary'
        else:
            return 'This is not Y or N'
    else:
        return 'There is no this word in dictionary'

word = input('Enter a word: ')

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
