# 공유기 설치

import sys
n, c = map(int, sys.stdin.readline().split())
a = [int(sys.stdin.readline()) for i in range(n)]
a.sort()

d_min = 1
d_max = a[n-1] - a[0]

while d_min <= d_max:
    d_mid = (d_min + d_max) // 2

    count = 1
    pre_loc = 0
    for i in range(1,len(a)):
        if a[i]-a[pre_loc] >= d_mid:
            count += 1
            pre_loc = i

    if count >= c:
        d_min = d_mid+1
    elif count < c:
        d_max = d_mid-1

print (d_max)


