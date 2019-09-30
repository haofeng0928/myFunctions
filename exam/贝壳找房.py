# # 第一题：相邻两数之差绝对值最小
# # n = int(input())
# # array = list(map(int, input().strip().split()))
# array = [1, 3, 4, 7, 2, 6, 5, 12, 32]
#
# tem = abs(array[0] - array[1])
# res = [array[0], array[1]]
# for i in range(1, len(array)-1):
#     dif = abs(array[i] - array[i+1])
#     if dif < tem:
#         tem = dif
#         res = [array[i], array[i+1]]
# print(res[0], res[1])


# # 第二题：两个数和表示
# # n = int(input())
# # array = list(map(int, input().strip().split()))
# array = [1, 2, 3, 4]
#
# count = 0
# array = sorted(array, reverse=True)
# for i in range(len(array)-2):
#     for j in range(i+1, len(array)-1):
#         if array[i] - array[j] in array[j+1:]:
#             count += 1
# print(count)


# 第三题：最长上升子序列
# N = int(input())
# nums = []
# for _ in range(N):
#     nums.append(int(input().strip()))
nums = [5, 1, 6, 8, 2, 4, 5, 10]  # 5

lens = len(nums)
if lens <= 1:
    print(lens)
dp = [1] * lens
for i in range(1, lens):
    for j in range(i):
        if nums[i] > nums[j]:
            print(nums[i], nums[j])
            dp[i] = max(dp[i], dp[j] + 1)
            print(dp[i])
print(max(dp))


# # 第四题：最小增加负荷
# def fun(a):
#     c = 0
#     for i in range(len(a)-1):
#         if a[i] >= a[i + 1]:
#             c += a[i] - a[i + 1] + 1
#             a[i + 1] = a[i] + 1
#     return c
#
#
# # N = int(input())
# # array = list(map(int, input().strip().split()))
# array = [1, 4, 3, 2, 5]  # 6
#
# max_index = array.index(max(array))
# array1 = array[:max_index]
# array2 = array[max_index:][::-1]
# res = fun(array1) + fun(array2)
# if array1[-1] == array2[-1]:
#     res += 1
# print(res)

