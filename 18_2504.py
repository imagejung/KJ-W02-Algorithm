#괄호의 값

#입력 받기
import sys
a = sys.stdin.readline()

ans = 0
tmp = 1
stk = []

for i in range(len(a)):
    # 괄호를 열어줄때는 닫아줄때 검증을 위해 스택에 넣고
    # 숫자 값 검토를 위해 (는 2를 곱해주고 [는 3을 곱해준다.
    if a[i] == '(':
        stk.append(a[i])
        tmp *= 2

    elif a[i] == '[':
        stk.append(a[i])
        tmp *= 3

    elif a[i] == ')':
        #틀린 괄호로 닫히면 답에 0 넣고 반복문 탈출
        if len(stk) == 0 or stk[-1] == '[':
            ans = 0
            break
        #()로 완벽히 닫히는 순간 우선 ans에 tmp값을 더해줌.괄호가 정확히 닫힐거라 예상하고..
        elif a[i-1] == '(':
            ans += tmp
        #괄호가 정상적으로 닫히고 있으면 닫힌 만큼 tmp값 원상복구 시켜주기
        #ans에 더해줘야 할 값은 '()'로 닫히는 순간 다 ans에 더해줌
        tmp //= 2
        stk.pop()

    elif a[i] == ']':
        if len(stk) == 0 or stk[-1] == '(':
            ans = 0
            break
        elif a[i-1] == '[':
            ans += tmp
        tmp //= 3
        stk.pop()

#스텍에 남은게 있으면 다 불완전한 괄호이므로 ans = 0
if len(stk) != 0:
    ans = 0
print(ans)