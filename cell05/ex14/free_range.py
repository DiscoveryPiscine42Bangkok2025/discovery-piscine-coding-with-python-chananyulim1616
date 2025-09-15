import sys
import re
if len(sys.argv)<2:
    print('none',end='')
else:
    print([i for i in range(int(sys.argv[1]), int(sys.argv[2])+1)])