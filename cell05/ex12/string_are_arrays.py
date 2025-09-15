import sys
import re
if len(sys.argv)<2:
    print('none',end='')
else:
    print(len(re.findall('z',sys.argv[1]))*'z',end='')