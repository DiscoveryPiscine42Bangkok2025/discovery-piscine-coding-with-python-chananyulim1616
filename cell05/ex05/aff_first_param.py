import sys
try:
    print(f'{sys.argv[1]}',end='')
except IndexError:
    print('none',end='')