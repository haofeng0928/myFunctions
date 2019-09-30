# 位运算
# &、|和and、or用来比较两组变量

# 如果a，b是数值变量，则&、|表示位运算，and、or则依据是否非0来决定输出
# and中含0则返回0，均为非0则返回后一个值
# or中至少有一个非0时，返回第一个非0
print(1 & 2, 1 | 2)
print(1 and 2, 1 or 2)

# 如果a, b是逻辑变量，则两类的用法基本一致
print((3 > 0) & (3 < 1))
print((3 > 0) | (3 < 1))
print((3 > 0) and (3 < 1))
print((3 > 0) or (3 < 1))

# n & 0xffffffff得到n的补码
# 正数不变，负数将符号为置零，变为正数
num = -9
print(num & 0xffffffff)

# 左移<<、右移>>
mask = 1
mask <<= 2
print(mask)

