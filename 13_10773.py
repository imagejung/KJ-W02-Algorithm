#제로

import sys
k = int(sys.stdin.readline())

stk = []
for i in range(k):
    n = int(sys.stdin.readline())

    if n == 0:
        stk.pop()
    else:
        stk.append(n)

cnt = 0
for i in stk:
    cnt += i

print(cnt)