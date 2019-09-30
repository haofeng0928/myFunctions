# 背包问题
w = [2, 2, 6, 5, 4]
v = [3, 6, 5, 4, 6]
m = 10

# s, m = map(int, input().split())
# w, v = [], []
# for _ in range(s):
#     tem = list(map(int, input().split()))
#     w.append(tem[0])
#     v.append(tem[1])


def fun(weight, value, weight_max):
    weight = [0] + weight
    value = [0] + value
    num = len(weight)
    bag = [[0 for _ in range(weight_max + 1)] for _ in range(num)]
    for i in range(1, num):
        for j in range(1, weight_max + 1):
            if weight[i] <= j:
                bag[i][j] = max(bag[i - 1][j - weight[i]] + value[i], bag[i - 1][j])
            else:
                bag[i][j] = bag[i - 1][j]
    return bag[-1][-1]


print(fun(w, v, m))

