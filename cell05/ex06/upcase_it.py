import sys
try:
    print(f'{sys.argv[1].upper()}',end='')
except IndexError:
    print('none',end='')