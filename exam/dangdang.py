# def can_jump(a):
#     return jump(a, len(a)-1)
#
#
# def jump(a, index):
#     if index == 0:
#         return 1
#     for i in range(index):
#         if a[i]+i >= index and jump(a, i):
#             return 1
#     return 0
#
#
# # arr = list(map(int, input().split(',')))
# arr = [2, 3, 1, 1, 4]
# print(can_jump(arr))

# # s1, s2, s3 = list(input().split())
# s1 = 'aabcc'
# s2 = 'dbbca'
# s3 = 'aadbbcbcac'
# s1, s2, s3 = list(s1), list(s2), list(s3)
# print(s1, s2, s3)
# flag = 1
# while s1 or s2:
#     if s1[0] != s3[0] and s2[0] != s3[0]:
#         flag = 0
#         break
#     while s1:
#         if s1[0] == s3[0]:
#             s1 = s1[1:]
#             s3 = s3[1:]
#         else:
#             break
#     while s2:
#         if s2[0] == s3[0]:
#             s2 = s2[1:]
#             s3 = s3[1:]
#         else:
#             break
# if flag:
#     print(1)
# else:
#     print(0)


def is_in(a1, a2, a3):
    len1 = len(a1)
    len2 = len(a2)
    len3 = len(a3)
    if len1 + len2 != len3:
        return 0
    dp = [[0] * (len2+1) for _ in range(len1+1)]
    for i in range(0, len1+1):
        for j in range(0, len2+1):
            if i == 0 and j == 0:
                dp[i][j] = 1
            elif i == 0:
                dp[i][j] = dp[i][j-1] and (a2[j-1] == a3[j-1])
            elif j == 0:
                dp[i][j] = dp[i-1][j] and (a1[i-1] == a3[i-1])
            else:
                dp[i][j] = (dp[i-1][j] and a1[i-1] == a3[i+j-1]) or (dp[i][j-1] and a2[j-1] == a3[i+j-1])
    return dp[len1][len2]


s1, s2, s3 = input().split()
if is_in(s1, s2, s3):
    print(1)
else:
    print(0)

