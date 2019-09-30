# # 记分板
# n = 6
# ac = 'ADEGHM'
# person = [58, 42, 98, 84, 84, 40, 75, 97, 98, 7, 8, 40, 54]
#
# # n = int(input())
# # ac = input()
# # person = list(map(int, input().strip().split()))
#
# dic = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
#        'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13}
# ac_index = []
# for item in ac:
#     ac_index.append(dic[item])
# print(ac_index)
# for i in ac_index:
#     person[i-1] = -1
# print(person)
# res = person.index(max(person))
# print(res+1)
# for i in dic:
#     if dic[i] == res + 1:
#         print(i)
#         break

# 学术交流
n, m, k = 3, 3, 2
array = [[2, 3], [3, 1]]
pos = [[0 for i in range(n)] for j in range(m)]
print(pos)
for item in array:
    pos[item[0]-1][item[1]-1] = 1
print(pos)

tem = 0
index = 0
for i in range(m):
    if sum(pos[i]) > tem:
        tem = sum(pos[i])
        index = i
