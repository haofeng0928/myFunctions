# 字符串匹配：增加、删除、替换
w1 = input()
w2 = input()
# w1 = 'abc'
# w2 = 'abd'
len1 = len(w1)
len2 = len(w2)
dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
for i in range(len1+1):
    dp[i][0] = i
for i in range(len2+1):
    dp[0][i] = i
for i in range(1, len1+1):
    for j in range(1, len2+1):
        if w1[i-1] == w2[j-1]:
            flag = 0
        else:
            flag = 1
        dp[i][j] = min(dp[i-1][j-1] + flag, min(dp[i-1][j]+1, dp[i][j-1]+1))
print(dp[-1][-1])

