#최대 힙

import sys
import heapq

n = int(sys.stdin.readline())

heap = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x:
        # heappush(list, value) 를 하면, 최소 힙 구성해 줌
        # 튜플의 0번째 인자인 -x를 기준으로 heap을 구성 -> 절대값이 클수록 -x는 더 작으니 최대 힙으로 활용할 수 있음
        heapq.heappush(heap, (-x, x))
    else:
        if len(heap) >= 1:
            print(heapq.heappop(heap)[1]) #-x가 아닌 x의 값을 출력하기 위해 튜플[1]자리 값 print
        else:
            print(0)
