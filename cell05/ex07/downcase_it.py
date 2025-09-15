import sys
try:
    print(f'{sys.argv[1].lower()}',end='')
except IndexError:
    print('none',end='')