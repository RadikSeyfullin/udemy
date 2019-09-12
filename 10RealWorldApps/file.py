with open('fruits.txt', 'a+') as myfile:
    myfile.seek(0)
    content = myfile.read()
    myfile.write(content)
