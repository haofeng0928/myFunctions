# 回文链表
# arr = list(map(int, input().split()))
# lens = len(arr)
# flag = True
# for i in range(lens // 2):
#     if arr[i] != arr[lens-i-1]:
#         flag = False
#         break
# print(flag)


# 薯片盒两端拿薯片，得快乐值
a = list(map(int, input().split()))
lens = len(a)
if lens % 2 == 0:
    print('Yes')
else:
    tem = sum(a[::2])
    if tem >= (sum(a) - tem):
        print('Yes')
    else:
        print('No')

