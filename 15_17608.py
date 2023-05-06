#막대기

import sys
n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for i in range(n)]

# ans배열. 답을 저장하는 배열
# 막대기의 오른쪽(a 배열의 끝)부터 ans배열과 비교하여 ans배열 마지막보다 크면 ans에 저장
ans = [a.pop()]
for i in range(n-1):
    tmp = a.pop()
    if ans[-1] < tmp:
        ans.append(tmp)

print(len(ans))