import sys
def greetings(text:str='noble stranger') -> str:
    if type(text) != str:
        print('Error! It was not a name.')
    else:
        print('Hello, ' + text)

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
