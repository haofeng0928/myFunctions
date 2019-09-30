# # 优先偶数的有序TOPN
# arr_str, N_str = input().split(';')
# arr = list(map(int, arr_str.split(',')))
# N = int(N_str)
#
# a, b = [], []
# for i in arr:
#     if i % 2 == 0:
#         a.append(i)
#     else:
#         b.append(i)
# a = sorted(a, reverse=True)
# b = sorted(b, reverse=True)
# res = a + b
# output = [str(i) for i in res[:N]]
# print(','.join(output))


# # 扑克游戏
# def is_in(mei, bai):
#     for i in bai:
#         if i not in mei:
#             return False
#     return True
#
#
# S = int(input())
# for _ in range(S):
#     mei = list(map(int, list(input())))
#     bai = list(map(int, list(input())))
#     print('{')
#     res = ''
#     res_list = []
#     flag = is_in(mei, bai)
#     if flag:
#         for item in mei:
#             if bai:
#                 if item not in bai:
#                     res += 'd'
#                 elif item == bai[0] and item == bai[-1]:
#
#                 elif item == bai[0]:
#                     res += 'l'
#                     bai = bai[1:]
#                 elif item == bai[-1]:
#                     res += 'r'
#                     bai = bai[:-1]
#         print(' '.join(res))
#     print('}')

