# 수 찾기
import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
m = int(input())
b = list(map(int, sys.stdin.readline().split()))

a.sort()

# 이분 탐색 로직
for i in range(m):
    pl, pr = 0, n-1

    while True:
        pc = (pl + pr) // 2
        if b[i] == a[pc]:
            print(1)
            break
        elif pl > pr:
            print(0)
            break

        elif b[i] > a[pc]:
            pl = pc + 1
        elif b[i] < a[pc]:
            pr = pc - 1


