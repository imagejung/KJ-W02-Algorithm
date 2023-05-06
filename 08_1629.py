# 곱셈

# a를 b번 곱한수를 c로 나눈 나머지 구하기
import sys
a, b, c = map(int, sys.stdin.readline().split())

def multi(a,b):
    if b == 1:
        return a % c
    else:
        tmp = multi(a, b//2) # 변수에 넣는것이 핵심. 시간복잡도 줄여줌.
        if b % 2 == 0:
            return (tmp * tmp) % c
        else:
            return (tmp * tmp * a) % c # (a%c) * (b%c) % c 와 (a%c) * b % c 는 같다.

print(multi(a,b))