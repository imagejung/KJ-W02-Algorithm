#행렬 제곱

#입력
import sys
n,b = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

#x행렬 곱하기 y행렬 수행하는 함수
def multi(x, y):
    z = [[0]*n for _ in range(n)] #z공간 배열 미리 만들어놔야 함
    for i in range(n):
        for j in range(n):
            tmp = 0
            for k in range(n):
                tmp += x[i][k] * y[k][j]
            z[i][j] = tmp % 1000
    return z

#분할정복으로 탐색
def square(a, b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                a[i][j] %= 1000
        return a

    else: #1이 아닌경우 쭉 분할
        tmp = square(a, b//2)
        if b % 2 == 0:
            return multi(tmp, tmp)
        else:
            return multi(multi(tmp, tmp), a)

ans = square(a,b)
for i in ans:
    print(*i)