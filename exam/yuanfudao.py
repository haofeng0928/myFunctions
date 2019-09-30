# 20190916
# # 逆时针打印数组
# N, M = map(int, input().split())
# arr = []
# for _ in range(N):
#     tem = list(map(int, input().split()))
#     arr.append(tem)
# # N, M = 3, 3
# # arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# res = []
# res += [arr[i][0] for i in range(len(arr))]
# arr = [item[1:] for item in arr]
# while arr:
#     new = []
#     for i in range(len(arr[0])):
#         tem = [arr[j][i] for j in range(len(arr))][::-1]
#         new.append(tem)
#     arr = new
#     res += [arr[i][0] for i in range(len(arr))]
#     arr = [item[1:] for item in arr]
# res = [str(i) for i in res]
# print(' '.join(res))

# 最长连续子序列
# n, s = map(int, input().strip().split())
# arr = list(map(int, input().strip().split()))
n, s = 6, 5
arr = [5, 1, 1, 1, 2, 3]
count = 0
for i in range(n):
    if arr[i] > s:
        continue
    for j in range(i, n):
        if sum(arr[i:j+1]) <= s:
            count = max(count, j+1-i)
        else:
            break
print(count)
