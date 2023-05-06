#가운데를 말해요

import sys
import heapq

n = int(sys.stdin.readline())
leftheap = [] #최대힙, 루트가 중간값, 전체배열중 낮은부분
rightheap = [] #최소힙, 루트가 중간값 바로 다음값. 전체배열중 높은부분

#leftheap 루트 > rightheap 루트 이면 루트끼리 교체 -> 중간값이 leftheap 루트에 자리잡음
for i in range(n):
    a = int(sys.stdin.readline())

    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap, (-a,a))
    else:
        heapq.heappush(rightheap, (a,a))

    #rightheap이 없는경우 예외처리 필요.
    if rightheap and leftheap[0][1] > rightheap[0][1]:
        left = heapq.heappop(leftheap)
        right = heapq.heappop(rightheap)

        heapq.heappush(leftheap,(-right[1],right[1]))
        heapq.heappush(rightheap, (left[1],left[1]))

    print(leftheap[0][1])

