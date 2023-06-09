#스택

import sys
n = int(sys.stdin.readline())
stk = []

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        stk.append(command[1])
    elif command[0] == 'pop':
        if len(stk) == 0:
            print(-1)
        else:
            print(stk.pop())
    elif command[0] == 'size':
        print(len(stk))
    elif command[0] == 'empty':
        if len(stk) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stk) == 0:
            print(-1)
        else:
            print(stk[-1])
