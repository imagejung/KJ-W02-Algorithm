#뱀
import copy
import sys
from collections import deque
n = int(sys.stdin.readline())

#사과 위치 입력
k = int(sys.stdin.readline())
k_list = [list(map(int, sys.stdin.readline().split())) for i in range(k)]

#뱀 이동 경로 입력
l = int(sys.stdin.readline())
l_list = [list(sys.stdin.readline().split()) for i in range(l)]
l_list = deque(l_list)
l_list.appendleft(['0','0'])
l_list.append([int(l_list[-1][0])+n,'0'])

loc = [1,1] # 뱀 머리
stk = deque([[1,1]]) # 뱀 스택
direction = 0 # 이동방향, 0123 동남서북
time = 0 # 게임 시간
finish = 0 # 게임 끝내는 플래그

for i in range(1, len(l_list)):
    if finish == 1:
        break

    # 한칸씩 한줄동안 이동하는 for문
    for j in range(int(l_list[i][0]) - int(l_list[i-1][0])):
        # 시간 세기
        time += 1

        # 방향에 맞게 이동
        if direction == 0:
            loc[1] += 1
        elif direction == 1:
            loc[0] += 1
        elif direction == 2:
            loc[1] -= 1
        elif direction == 3:
            loc[0] -= 1

        # 벽에 부딪히거나 자기 몸에 부딪히면 게임 끝
        if loc[0] == 0 or loc[0] == n+1 or loc[1] == 0 or loc[1] == n+1:
            finish = 1
            break
        elif loc in stk: #자기 몸에 부딪히는 경우
            finish = 1
            break

        # 머리 좌표 에 넣어주기, deque이기 때문에 깊은 복사 필요
        stk.append(copy.deepcopy(loc))

        # 사과를 만난게 아니면 큐에서 꼬리 지우기 / 사과 지우기
        if not stk[-1] in k_list:
            stk.popleft() # 꼬리지우기
        else:
            k_list.remove(stk[-1]) #사과 지우기

    # 한 줄 이동(위 for문 다 돈)후, 방향 변경
    if l_list[i][1] == 'D':
        direction = (direction + 1) % 4
    elif l_list[i][1] == 'L':
        direction = (direction - 1) % 4

print(time)




