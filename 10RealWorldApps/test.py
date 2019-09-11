def sentence_maker(phrase):
    interrogatives = ('how', 'what', 'why')
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

results = []

while True:
    userinput = input('Say something: ')
    if userinput == '\\end':
        break
    else:
        results.append(sentence_maker(userinput))

print(' '.join(results))
