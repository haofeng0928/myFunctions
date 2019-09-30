# 字典内的每个单词都包含n个'a'和m个'z', 并且所有单词按照字典序排列。
# 小易现在希望你能帮他找出第k个单词是什么。


# n个'a'和m个'z'组合的可能性，n、m位置互换不影响结果
def count_nm(a, b):
    ans = 1
    for i in range(a + 1, a + b + 1):
        ans *= i
    for j in range(1, b + 1):
        ans //= j
    return ans


# n, m, k = 2, 2, 6
n, m, k = map(int, input().strip().split())

if count_nm(n, m) < k:
    print(-1)
else:
    res = ''
    while n > 0 and m > 0:
        # 假设第一位为'a'
        cnt = count_nm(n-1, m)
        # 单词不足k时，第一位设置为z
        if cnt < k:
            k -= cnt
            res += 'z'
            m -= 1
        else:
            res += 'a'
            n -= 1
    res += 'a' * n
    res += 'z' * m
    print(res)

