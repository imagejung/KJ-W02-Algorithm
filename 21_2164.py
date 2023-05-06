#카드2

import sys
from collections import deque

n = int(sys.stdin.readline())
a = deque([])

# n이 1일 경우 따로 처리
if n == 1:
    print(1)
else:
    for i in range(n): #1~n 배열 만들어줌
        a.append(i+1)

    while True:
        a.popleft() # 카드 한장 버리고
        a.append(a.popleft()) # 카드 한 장 뒤로 보내고
        if len(a) == 1: # 카드가 한 장 남을때 까지
            break

    print(a[0])