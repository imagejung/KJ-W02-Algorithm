#괄호

import sys
t = int(sys.stdin.readline())

cnt = 0
for i in range(t):
    stk = []
    a = sys.stdin.readline()
    flag = 0
    for i in range(len(a)):

        if a[i] == '(':
            stk.append(a[i])
        elif a[i] == ')':
            if len(stk) == 0:
                flag = -1
            elif stk[-1] == '(':
                stk.pop()

    # () 순서가 틀리지 않고, (가 쌍으로 다 빠져나갔으면
    if flag == 0 and len(stk) == 0 :
        print("YES")
    else:
        print("NO")