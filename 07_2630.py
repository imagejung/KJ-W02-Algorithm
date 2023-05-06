#색종이 만들기

import sys

# 입력 받는 부분
n = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

white, blue = 0, 0

# 길이가 n인 정사각형이 동일한 색인지 확인
def cut (x, y, n) :
    global white, blue
    color = a[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            # 조건이 맞지 않을 때 4개로 쪼개서 풀어버리는 분할 정복
            # 길이를 반으로, 총4개로 쪼개서 재귀함수 호출
            if color != a[i][j]:
                cut(x, y, n//2)
                cut(x, y+n//2, n//2)
                cut(x+n//2, y, n//2)
                cut(x+n//2, y+n//2, n//2)
                return
    # 쪼개지 않고(재귀함수 호출하지 않고) 동일한 색인게 확인되면 카운트 +
    if color == 0:
        white += 1
    else:
        blue += 1

cut(0,0,n)
print(white)
print(blue)