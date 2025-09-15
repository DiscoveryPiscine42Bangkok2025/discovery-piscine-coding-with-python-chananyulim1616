import sys
import re
if len(sys.argv)<2:
    print('none',end='')
else:
    print('parameters:', len(sys.argv[1:]))
    for i in sys.argv[1:]:
        print(f'{i}: {len(i)}')