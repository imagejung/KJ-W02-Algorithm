#탑

import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
stk = []

for i in range(n):
    while stk:
        if stk[-1][1] > a[i]: #스택에(직전까지 쌓여온 탑)중 검토하는 탑보다 큰 탑을 출력
            print(stk[-1][0]+1)
            break
        else:
            stk.pop() #검토하는 i탑보다 작으면 지움.(어차피 뒤에도 i탑에 가림)
    if not stk:
        print(0)
    stk.append([i, a[i]]) #다음 검토를 위하여 스택에 i탑 넣기