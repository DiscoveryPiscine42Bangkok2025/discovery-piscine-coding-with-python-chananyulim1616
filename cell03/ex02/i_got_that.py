txt_input = input('What you gotta say? : ')
if txt_input != 'STOP':
    while True:
        txt_input = input(f'I got that! Anything else? : ')
        if txt_input == 'STOP':
            break