# n, m, d = 6, 2, 3
# special = [2, 1]
# num = [3, 4, 5, 6, 1]
#
#
# list(map(int, input().strip().split()))


n = 6
s = '3 + 2 + 1 + -4 * -5 + 1'
s = s.split()
print(s)


def sort_num(num, i, j):
    tem = sorted(num[i:j+1])
    num = num[:i] + tem + num[j+1:]
    return num


num, ops = [], []
for i in range(len(s)):
    if i % 2 == 0:
        num.append(int(s[i]))
    else:
        ops.append(s[i])
print(num, ops)
op1 = ['+', '-']
op2 = ['*', '/']
count = 10
while count:
    for i in range(len(ops)-1):
        if ops[i] == '+' and ops[i+1] in op1:
            if num[i] > num[i+1]:
                num[i], num[i+1] = num[i+1], num[i]
            print('num+', num)
        elif ops[i] == '*' and ops[i+1] in op2:
            if num[i] > num[i+1]:
                num[i], num[i+1] = num[i+1], num[i]
            print('num*', num)
    count -= 1
print(num, ops)

