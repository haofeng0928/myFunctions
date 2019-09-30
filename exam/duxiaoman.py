# 20190915
# # 传送门
# # N, A, B, C = map(int, input().split())
# # arr = list(map(int, input().split()))
# N, A, B, C = 7, 1, 1, 1
# arr = [3, 6, 4, 3, 4, 5, 6]
# arr = [0] + arr
# dis = [arr[i]-i for i in range(N+1)]
# max_dis = max(dis)
# max_index = dis.index(max_dis)
# cost = 0
# if arr[1] > max_index:
#     cost += (arr[1]-max_index) * B
# cost += A
# if arr[max_index] < N:
#     max_d = max(dis[arr[max_index]:])
#     max_i = dis.index(max_d)
#     count = (max_i-max_index) * C + A + (N-arr[max_i]) * B
#     tem = min((N-arr[max_index]) * C, count)
#     cost += tem
# cost += A
# print(cost)

# 纸片博弈
while True:
    x, y = map(int, input().split())
    x = x % 4 if x % 4 != 0 else 4
    y = y % 4 if y % 4 != 0 else 4
    if x == 1 or y == 1:
        print('WIN')
    else:
        WIN = [[4, 2], [4, 3]]
        LOSE = [[4, 4], [3, 3], [3, 2], [2, 2]]
        if [x, y] in WIN or [y, x] in WIN:
            print('WIN')
        else:
            print('LOSE')
