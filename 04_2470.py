# # 두 용액 (미완성)
# import sys
#
# n = int(sys.stdin.readline())
# a = list(map(int, sys.stdin.readline().split()))
# a.sort()
# ans = [1000000000, 0, 0]
# flag = 1
#
# #음수, 양수 모두 있을 떄
# if a[0] * a[n-1] < 0:
#     for i in range(n-1):
#         if a[i] * a[i+1] < 0:
#             base_p = i+1
#             base_m = i
#             break
#
#         # 0이 있을 때
#         if a[i] * a[i+1] == 0:
#             if abs(a[i+1] + a[i+2]) < abs(a[i]+a[i+1]):
#                 print(a[i+1], a[i+2])
#             else:
#                 print(a[i], a[i+1])
#             flag = 0
#             break
#
#     while True:
#         if flag == 0:
#             break
#         else:
#             if abs((a[base_p] + a[base_m])) < ans[0]:
#                 ans[0] = (a[base_p] + a[base_m])
#                 ans[1] = base_m
#                 ans[2] = base_p
#
#             if base_m == 0 and base_p == n-1:
#                 print(a[ans[1]], a[ans[2]])
#                 break
#
#             if (a[base_p] + a[base_m]) == 0:
#                 print(a[base_m], a[base_p])
#                 break
#             elif (a[base_p] + a[base_m]) > 0:
#                 if base_m != 0:
#                     base_m = base_m - 1
#             elif (a[base_p] + a[base_m]) < 0:
#                 if base_p != n-1:
#                     base_p = base_p + 1
#
# # 0이 있으면서 맨 끝에 있을 때
# elif a[0] * a[n-1] == 0:
#     if a[0] == 0:
#         print(a[0], a[1])
#     else:
#         print(a[n-2], a[n-1])
#
#
# # 음수 또는 양수로만 이루어져 있을 때
# else:
#     if (abs(a[0] + a[1]) < abs(a[-1] + a[-2])):
#         print(a[0], a[1])
#     else:
#         print(a[-2], a[-1])
#
