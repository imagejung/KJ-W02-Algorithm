# 사냥꾼

# 입력 받기 (m = 사대수, n = 동물수, l = 사정거리)
import sys
m, n, l = map(int, sys.stdin.readline().split())
m_loc = list(map(int, sys.stdin.readline().split()))
m_loc.sort()
cnt = 0

# 이분탐색을 통해 동물의 x좌표 왼쪽,오른쪽 사대를 찾음
for i in range(n):
    n_x, n_y = map(int, sys.stdin.readline().split())

    lo, hi = 0, m-1
    left, right = 0,0
    while (lo+1 < hi):
        mid = (lo + hi) // 2
        if n_x >= m_loc[mid]:
            lo = mid
        else:
            hi = mid

    # 찾은 왼쪽 오른쪽 사대에서 동물이 사정거리 안에 있는지 확인
    if abs(n_x - m_loc[lo]) + n_y <= l or abs(n_x - m_loc[hi]) + n_y <= l:
        cnt += 1

print(cnt)

