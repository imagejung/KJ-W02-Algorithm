# 가장 긴 증가하는 수열 (이진탐색) // Dynamic Programming으로도 풀 수 있음.

import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
d = [a[0]]

# GoodNotes에 따로 로직 설명.
for i in range(1, n):
    # a[i]가 답을 저장하는 d수열의 마지막 값보다 크면 그냥 붙이기
    if a[i] > d[-1]:
        d.append(a[i])
    else: # a[i]<d[-1], d수열 내부에서 a[i]보다 작은수 중 가장 큰 수 다음에 a[i] 넣기. (이진탐색으로 검색)
        lo, hi = 0, len(d)-1
        mid = (lo + hi) // 2
        tmp = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if d[mid] < a[i]:
                lo = mid + 1
            else:
                hi = mid -1
                tmp = mid
        d[tmp] = a[i]

print(len(d))


