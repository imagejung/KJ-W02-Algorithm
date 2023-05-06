# 공유기 설치
import sys
n, c = map(int, sys.stdin.readline().split())
a = [int(sys.stdin.readline()) for i in range(n)]
a.sort()

# 최적의 거리를 이분탐색을 통해 탐색
d_min = 1
d_max = a[n-1] - a[0]


while d_min <= d_max:
    d_mid = (d_min + d_max) // 2

    count = 1 # 첫 집에 공유기 설치하고 시작
    pre_loc = 0 # 직전 공유기 설치 위치 확인용
    for i in range(1, len(a)):
        if a[i]-a[pre_loc] >= d_mid: # 이분 탐색으로 정한 거리보다 멀면 공유기 설치
            count += 1 # 공유기 숫자 + 1
            pre_loc = i # 공유기 설치 위치 업데이트

    if count >= c: # 공유기가 너무 많이 만들어지면, 최소 거리를 늘리기
        d_min = d_mid+1
    elif count < c: # 공유기가 적게 만들어지면, 최소 거리를 줄이기
        d_max = d_mid-1

print (d_max)


