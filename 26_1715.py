#카드 정렬하기

import sys
import heapq

n = int(sys.stdin.readline())
cards = []
ans = 0

#힙으로 입력받아서 카드 리스트 만들기
for i in range(n):
    heapq.heappush(cards, int(sys.stdin.readline()))

#최소값 2개 받아서 더한 값 1)ans에 더하고 2)다시 카드리스트에 넣기
while len(cards) > 1:
    tmp = heapq.heappop(cards) + heapq.heappop(cards)
    ans += tmp
    heapq.heappush(cards, tmp)

print(ans)