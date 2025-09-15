import sys
import re
if len(sys.argv)<3:
    print('none',end='')
else:
    print(len(re.findall(sys.argv[1], sys.argv[2])),end='')