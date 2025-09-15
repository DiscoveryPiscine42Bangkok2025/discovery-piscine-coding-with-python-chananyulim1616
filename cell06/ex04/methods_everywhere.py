import sys
def shrink(text:str) -> str:
    return text[:8]
def enlarge(text:str) -> str:
    return f'{text:Z<8}'

if len(sys.argv)<2:
    print('none',end='')
else:
    for i in sys.argv[1:]:
        if len(i)>8:
            print(shrink(i))
        else:
            print(enlarge(i))