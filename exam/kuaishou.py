# 字符串
str1 = input()
str2 = input()
len1, len2 = len(str1)+1, len(str2)+1
dp = [[0 for _ in range(len2)] for _ in range(len1)]
for i in range(len2):
    dp[0][i] = i
for i in range(len1):
    dp[i][0] = i
for i in range(1, len1):
    for j in range(1, len2):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
print(dp[-1][-1])

# 1-9的数字
# s = []
# for _ in range(9):
#     tem = input()
#     s.append(tem)
s = ['53XX7XXXX',
     '6XX195XXX',
     'X98XXXX6X',
     '8XXX6XXX3',
     '4XX8X3XX1',
     '7XXX2XXX6',
     'X6XXXX28X',
     'XXX419XX5',
     'XXXX8XX79']


def fun(res):
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    tem = []
    for i in res:
        for j in i:
            if j in nums:
                if j not in tem:
                    tem.append(j)
                else:
                    return False
            elif j != 'X':
                return False
    return True


s = [list(item) for item in s]
res = [item for item in s]
for i in range(9):
    tem = [s[j][i] for j in range(9)]
    res.append(tem)
for i in range(3):
    for j in range(3):
        res.append([s[3*i][3*j], s[3*i][3*j+1], s[3*i][3*j+2],
                    s[3*i+1][3*j], s[3*i+1][3*j+1], s[3*i+1][3*j+2],
                    s[3*i+2][3*j], s[3*i+2][3*j+1], s[3*i+2][3*j+2]])
for i in res:
    print(i)
if fun(res):
    print('true')
else:
    print('false')
