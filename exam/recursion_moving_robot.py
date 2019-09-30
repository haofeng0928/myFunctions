# 一个m行和n列的方格，一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格
# 但是不能进入行坐标和列坐标的数位之和大于k的格子。
# 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
# 但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？


def moving(x, y):
    if not (0 <= x < rows) or not (0 <= y < cols) or array[x][y] == 1 or sum(map(int, str(x) + str(y))) > thresh:
        return 0
    array[x][y] = 1
    return 1 + moving(x-1, y) + moving(x+1, y) + moving(x, y-1) + moving(x, y+1)


rows, cols = map(int, input().split())
thresh = int(input())

array = [[0 for col in range(cols)] for row in range(rows)]
print(moving(0, 0))

