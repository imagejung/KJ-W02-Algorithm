#가장 가까운 두 점

import sys
n = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

#x좌표 기준으로 정렬
a.sort()

def distance (x,y):
    return (y[0] - x[0])**2 + (y[1] - x[1])**2

def mindist (left, right):
    #나누다가 한점만 생기면 케이스 고려하지 않기 위해 최대값 반환
    if left == right:
        return sys.maxsize
    #두점만 있으면 거리 반환
    if right - left == 1:
        return distance(a[left],a[right])

    #분할정복으로 최솟값 찾음
    mid = (left + right) // 2
    result = min(mindist(left, mid), mindist(mid, right))

    #분할되는 경계를 기준으로 좌우에 위치한 점들이 쌍이 최솟값일수도 있음. 검토 필요
    #mid기준으로 x좌표 거리제곱이가 result(현재 최소값)보다 작은것만 tmp_list에 넣음
    tmp_list = []
    for i in range(left, right+1):
        if result > (a[mid][0] - a[i][0])**2:
            tmp_list.append(a[i])

    #tmp_list를 y기준으로 정렬하여
    tmp_list.sort(key = lambda x:x[1])

    # tmp_list내에서 최소값 검토, 기존 최소값이랑 비교하여 최소값 업데이트
    for i in range(len(tmp_list)-1):
        for j in range(i+1, len(tmp_list)):
            if (tmp_list[j][1] - tmp_list[i][1])**2 < result:
                result = min(result, distance(tmp_list[i],tmp_list[j]))
            else:
                break

    return result

print(mindist(0,n-1))