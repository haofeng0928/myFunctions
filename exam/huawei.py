# 输入字符串，输出去重的合法字符串和非法字符串、合法字符串循环左移10次并按ASCII排序

strs = input()
legal = []
illegal = []
n = 10

# 输出去重的合法字符串和非法字符串
for i in strs:
    if i.isalnum():
        if i not in legal:
            legal.append(i)
    else:
        illegal.append(i)
print(''.join(legal))
print(''.join(illegal))

# 合法字符串循环左移10次
if len(legal) < n:
    n = n % len(legal)
legal_left = legal[n:] + legal[:n]
print(''.join(legal_left))

# ASCII排序
legal_sort = sorted(legal)
print(''.join(legal_sort))

# 一行输入多个字符串，字符串通过空格分开，第一个字符为字符串的数量
# 将每个字符串分割成长度为8的子字符串，子字符串长度不足8时后面补0
# 最后对分割后的所有子字符串排序，并以空格作为间隔输出

str_in = input()
str_list = str_in.strip().split()

str_out = []

for line in str_list[1:]:
    count = len(line) // 8
    for i in range(count):
        str_out.append(line[i * 8:(i + 1) * 8])

    if count * 8 < len(line):
        tem = line[count * 8:]
        for j in range(8 - len(tem)):
            tem += '0'

        str_out.append(tem)

str_out.sort()

res = ' '.join(str_out)
print(res)


# 输入一个字符串，将括号里面的字符串复制括号前的数字次，并反序输出
# abc3(A)
def out_s(s):
    res = []
    for i in s:
        if i == ']':
            current = []
            while res[-1] != '[':
                current.append(res.pop())
            res.pop()
            mul, ind = 0, 0
            while res and res[-1].isdigit():
                mul += int(res.pop()) * pow(10, ind)
                ind += 1
            res += current[::-1] * mul
        else:
            res.append(i)
    res.reverse()
    return res


if __name__ == '__main__':
    s = input()
    s = s.replace('(', '[')
    s = s.replace('{', '[')
    s= s.replace(')', ']')
    s = s.replace('}', ']')
    res = out_s(s)
    print(''.join(res))


# 题目：输入多个一维数组，每次取这些一维数组的前n个元素放入一个新的一维数组，直到取完所有元素

def newMerge(lenth, lines):
    lines_len = len(lines)
    result = []

    # 进入循环
    count = 1
    while count > 0:

        # 遍历每行数组
        for i in range(len(lines)):

            # 第i行数组的长度
            len_ = len(lines[i])

            for j in range(min(lenth, len_)):
                # 依次添加min(lenth, len_)个元素，同时删除添加过的元素
                result.append(lines[i][0])
                del lines[i][0]

        # 统计数组中元素个数
        count = 0
        for m in range(len(lines)):
            for n in range(len(lines[m])):
                count += 1

    return result


if __name__ == '__main__':
    #     # 输入每次处理的长度
    #     lenth = int(input().strip())

    #     # 输入多行数组
    #     lines = []
    #     line = input()
    #     while line != '':
    #         line = line.split(',')
    #         line = [int(i) for i in line]
    #         lines.append(line)
    #         line = input()

    #     print(lines)

    lenth = 4
    lines = [[1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6]]
    print(newMerge(lenth, lines))

