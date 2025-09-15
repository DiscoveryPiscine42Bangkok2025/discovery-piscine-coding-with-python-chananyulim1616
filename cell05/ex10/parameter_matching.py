import sys
import re
if len(sys.argv)<2:
    print('none',end='')
else:
    txt_input = input('What was the parameter? ')
    if txt_input == sys.argv[1]:
        print('Good job!',end='')
    else:
        print('Nope, sorry...',end='')