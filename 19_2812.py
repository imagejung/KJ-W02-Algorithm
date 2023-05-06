#크게 만들기

import sys

n,k = map(int, sys.stdin.readline().split())
a = list(input())
ans = []

for i in range(n):
    #ans 스택에 답을 계속 만들어 넣음
    #ans스택 마지막 자리보다 a[i]가 크면 계속 while문 돌면서 지우고
    #k도 남아있고, ans스택도 있고, ans마지막 자리가 a[i]보다 작으면 ans계속 지움
    while k>0 and ans and ans[-1] < a[i]:
        ans.pop()
        k-=1
    #위의 조건들 다 맞으면 a[i] ans에 push
    ans.append(a[i])

print(''.join(ans[:len(ans)-k]))