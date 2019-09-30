# sorted(iterable[, cmp[, key[, reverse]]])
"""
对一个iterable对象排序，返回一个排序之后的list
@param iterable 可迭代遍历对象
@param cmp 默认None, 自定义的比较函数，2个参数
@param key 默认None, 自定义的函数，1个参数，参数值来源与列表元素
@param reverse 默认False(正序)
@return 返回一个排序之后的list
"""

# list排序，并保存index
arr = [55, 44, 33, 22, 11]
arr = [list(i) for i in zip(range(1, len(arr) + 1), arr)]
arr = sorted(arr, key=lambda x: x[1])
print('list = ', arr)

# tuple排序
t = (("e", 1), ("d", 2), ("c", 3), ("b", 4), ("a", 5))
t = sorted(t, key=lambda item: item[0])
print('tuple = ', t)

# 字典排序
d = {'e': 1, 'd': 2, 'c': 3, 'b': 4, 'a': 5}
print(d.keys(), d.values())  # 分别取出字典中的键值
print(d, d.items())  # d为字典，d.items()为列表
print(sorted(d))  # sorted默认对键进行排序，并返回键的有序列表
print(sorted(d.keys()), sorted(d.values()))
d = sorted(d.items(), key=lambda item: item[0])
print('dict = ', d)

# itemgetter代替lambda，支持多级排序
from operator import itemgetter
t = (("e", 1), ("d", 2), ("c", 3), ("b", 4), ("a", 5), ("a", 0))
print(sorted(t, key=itemgetter(0, 1)))

