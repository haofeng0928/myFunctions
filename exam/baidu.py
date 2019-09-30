# 踢球
n, m = 3, 3
arr = [[1, 5], [2, 6], [7, 8]]
point = [2, 4, 8]
# n, m = map(int, input().split())
# arr = []
# for _ in range(n):
#     a = list(map(int, input().split()))
#     arr.append(a)
# point = []
# for _ in range(m):
#     point.append(int(input()))
arr = sorted(arr)
point = sorted(point)
count = 0
for i in range(m):
    for j in range(len(arr)):
        if arr[j][0] <= point[i] <= arr[j][1]:
            count += 1
            arr.remove(arr[j])
            break
arr = arr[::-1]
point = point[::-1]
count2 = 0
for i in range(m):
    for j in range(len(arr)):
        if arr[j][0] <= point[i] <= arr[j][1]:
            count2 += 1
            arr.remove(arr[j])
            break
print(max(count, count2))

# # 跳跃递推
# a1, a2, a3, a4, n = 1, 2, 3, 4, 20
# # a1, a2, a3, a4, n = map(int, input().split())
# tem = [1, 1, 0, 1]
# while n > 4:
#     a = a1 + a2 + a4
#     a1, a2, a3, a4 = a2, a3, a4, a
#     n -= 1
# print(a4 % (10**9+7))
