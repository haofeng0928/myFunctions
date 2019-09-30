# 水源出水
# T = int(input())
# for k in range(T):
#     n, m, a, b, c = map(int, input().split())
#     arr = [[0 for _ in range(m)] for _ in range(n)]
# # n, m, a, b, c = 3, 4, 1, 2, 3
# # arr = [[0 for _ in range(m)] for _ in range(n)]
#     arr[a][b] = c
#     for i in range(n):
#         for j in range(m):
#             dis = abs(a-i) + abs(b-j)
#             arr[i][j] = c-dis if c > dis else 0
#     print('Case #%d:' % (k+1))
#     for i in range(n):
#         arr[i] = [str(item) for item in arr[i]]
#         print(' '.join(arr[i]))

# 矩阵操作
# 方法一：numpy，测试不通过
import numpy as np
n, m = 2, 2
A = [[1, 2], [3, 4]]
B = [[4, 3], [2, 1]]
A = np.array(A)
B = np.array(B)
res = np.dot(A.T, B)
res = np.dot(res, B.T).T
res = res.tolist()
n_c, m_c = n, m
print(' '.join([str(n_c), str(m_c)]))
for item in res:
    print(' '.join([str(i % 1009) for i in item]))
# 方法二：zip+矩阵乘法
def transpose(a):
    return list(map(list, zip(*a)))


def multi(a, b):
    n, m = len(a), len(b[0])
    ans = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            ans[i][j] = sum([a[i][k]*b[k][j] for k in range(len(a[i]))])
    return ans


print(' '.join(map(str, [n, m])))
res = multi(multi(B, transpose(B)), A)
for i in range(n):
    print(' '.join(map(lambda x: str(x % 1009), res[i])))

# 计数
# T = int(input())
# for k in range(T):
#     n, m = map(int, input().split())
#     arr = list(map(int, input().split()))
#     lr = []
#     for _ in range(m):
#         tem = list(map(int, input().split()))
#         lr.append(tem)
#     print('Case #%d:' % (k+1))
#     for i in range(n):
#         count = 0
#         for j in range(m):
#             if lr[j][0] <= arr[i] <= lr[j][1]:
#                 count += 1
#         print(count)

# CTC概率
# N, M, K = map(int, input().split())
# lk = list(map(int, input().split()))
# dis = []
# for _ in range(N):
#     tem = list(map(int, input().split()))
#     dis.append(tem)
# res = []
# count = K
# print(200)
