#철로

import sys
import heapq

#입력 받기, 집/사무실 상관없이 작은 수가 앞으로 오도록
n = int(sys.stdin.readline())
a = [sorted(list(map(int, sys.stdin.readline().split()))) for i in range(n)]
d = int(sys.stdin.readline())

#값의 index 1인 값(큰값)을 기준으로 오름차순 정렬
a.sort(key=lambda x : x[1])

ans = []
max = 0
#라인 스위핑
for i in range(n):
    #index 1인 값(큰값)을 기준으로 검토.
    #맞으면 ans힙에 추가
    #아래 while문에서 그동안 힙에 추가돼 있던 답만 다시 검토
    if(a[i][0] >= a[i][1] - d ):
        heapq.heappush(ans, (a[i][0], a[i][1]))

    #heap으로 가장 작은값 (가장 먼값)검토
    #맞으면 나머지도 다 가능
    #틀리면 pop하고 다음 가장 작은값 검토
    while len(ans)>1:
        if ans[0][0] < a[i][1] - d:
            heapq.heappop(ans)
        else:
            break

    #ans힙 다 검토 끝나면 max 값 검토
    if len(ans) > max:
        max = len(ans)

print(max)