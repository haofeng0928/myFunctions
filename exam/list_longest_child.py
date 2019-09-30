# 输入包含n个正整数m（1≤n≤10000）
# 输出最长递增子序列的长度

# bisect模块用于插入元素到有序列表。
# Bisect使用二分法排序，将待插入的元素插入到合适的位置
# bisect.bisect_left(a, x, lo=0, hi=len(a))  返回将x插入到列表a中的索引位置，如果已有x，则返回第一个x的位置

import bisect

# a = list(map(int, input().split()))
a = [7, 1, 3, 5, 2, 8, 9, 9, 8, 8, 4]

res = []
for i in a:
    pos = bisect.bisect_left(res, i)  # 返回将i插入到有序列表q中的index
    if pos == len(res):
        res.append(i)
    else:
        res[pos] = i  # 用i替换相应index的值，不改变最长递增子序列的长度

print(len(res))


tem = []
for i in range(len(a)-1):
    lens = len(a) - i
    b = [item for item in a]
    for j in range(i, len(a)-1):
        if b[j+1] <= b[j]:
            lens -= 1
            b[j+1] = b[j]
    tem.append(lens)

print(max(tem))


# 该思路同bisect模块
res = [a[0]]
for i in range(1, len(a)):
    if a[i] > res[-1]:
        res.append(a[i])
    elif a[i] == res[-1]:
        continue
    else:
        for j in range(len(res)-1, -1, -1):
            if len(res) == 1:
                res[j] = a[i]
            elif a[i] == res[j]:
                break
            elif a[i] < res[j]:
                continue
            else:
                res[j+1] = a[i]
                break
    print(res)
print(a)
print(len(res))

