# 두 용액
import sys

# 입력값 받고 소팅
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()

# 이분탐색 포인트 생성
left, right = 0, n-1
answer = 10000000000
answer_left, answer_right = 0, 0 # 양쪽 끝에서 시작

while right > left:
    if abs(a[left] + a[right]) < answer: # 탐색하면서 0보다 더 가까운 수가 만들어 지면 값 변경
        answer = abs(a[left] + a[right])
        answer_left, answer_right = left, right

    # 소팅 했으므로 배열 양쪽pair로 절대값이 유사
    # 배열 양쪽에서 하나씩 뽑아서 더하면서, 절대값이 큰쪽을 가운데로(절대값이 작은대로) 이동시켜 줌
    if a[left] + a[right] > 0:
        right = right - 1
    elif a[left] + a[right] < 0:
        left = left + 1
    elif a[left] + a[right] == 0:
        answer_left, answer_right = left, right
        break

print(a[answer_left], a[answer_right])