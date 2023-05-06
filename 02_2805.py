# 나무 자르기
import sys

t, n = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

sum_a = sum(a)
result = 0
pl, pr = 1, max(a)

# 이분 탐색으로 나무 자르기
while pl <= pr:
    pc = (pl + pr) // 2

    result = 0
    for i in a:
        if i >= pc:
            result += (i-pc)

    if result >= n:
        pl = pc + 1
    elif result < n:
        pr = pc - 1

print(pr)



