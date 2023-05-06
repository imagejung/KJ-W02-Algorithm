#요세푸스 문제0

import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
a = deque([])
ans = []

# 1~n 배열 만들어줌
for i in range(n):
    a.append(i+1)

#k-1 만큼 뽑아서 뒤로 보내고, k번째 수 ans배열로 보냄.
while True:
    for i in range(k-1):
        a.append(a.popleft())
    ans.append(a.popleft())
    if len(a) == 0:
        break

#답 출력..
print("<", end="")
for i in range(n-1):
    print(ans[i], end=", ")
print(ans[-1], end="")
print(">")

