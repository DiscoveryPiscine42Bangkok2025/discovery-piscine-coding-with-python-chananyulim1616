import sys
import re
if len(sys.argv)<2:
    print('none',end='')
else:
    for i in sys.argv[1:]:
        if i.endswith('ism'):
            pass
        else:
            print(i+'ism')