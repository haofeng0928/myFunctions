def find_longest(inp):
    res = []
    lens = ''
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for char in inp:
        if char not in nums:
            res.append(lens)
            lens = ''
        else:
            lens += char
    x = ''
    le = 0
    for chars in res:
        if len(chars) > le:
            x = chars
            le = len(chars)
    return str(le) + '/' + x


while True:
    s = input()
    res = find_longest(s)
    print(res)