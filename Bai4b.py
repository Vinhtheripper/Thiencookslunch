h=5
for i in range(1,h+1):
    for j in range(1,h+1-i):
        print('',end=' ')
    for k in range(1,i+1):
        print('+',end=' ')
    print()
for i in range(h - 1,0, -1):
    for j in range(1, h + 1 - i):
        print('', end=' ')
    for k in range(1, i + 1):
        print('+', end=' ')
    print()





