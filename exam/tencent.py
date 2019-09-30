# 栅栏最短长度
n, k = map(int, input().strip().split())
h = list(map(int, input().strip().split()))
lens = len(h)
init = sum(h[:k])
index = 1
for i in range(k, lens):
    tem = init + h[i] - h[i-k]
    if tem < init:
        init = tem
        index = i - k + 2
print(index)
