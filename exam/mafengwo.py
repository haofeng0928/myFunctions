# 最少花费
class Solution:
    def __init__(self, X, start_node):
        self.X = X
        self.start_node = start_node
        self.array = [[0] * (2 ** (len(self.X) - 1)) for i in range(len(self.X))]

    def transfer(self, sets):
        su = 0
        for s in sets:
            su = su + 2 ** (s - 1)
        return su

    def tsp(self):
        s = self.start_node
        num = len(self.X)
        cities = list(range(num))

        cities.pop(cities.index(s))
        node = s
        return self.solve(node, cities)

    def solve(self, node, future_sets):

        if len(future_sets) == 0:
            return self.X[node][self.start_node]
        d = 99999999
        distance = []

        for i in range(len(future_sets)):
            s_i = future_sets[i]
            copy = future_sets[:]
            copy.pop(i)
            distance.append(self.X[node][s_i] + self.solve(s_i, copy))

        d = min(distance)

        next_one = future_sets[distance.index(d)]

        c = self.transfer(future_sets)

        self.array[node][c] = next_one

        return d


if __name__ == '__main__':
    ss = '0,1,2,3#1,0,4,4#5,4,0,2#5,2,2,0'
    # ss = input()
    ss = ss.split('#')
    ss = [s.split(',') for s in ss]
    ans = Solution(ss, 0)
    print(float(ans.tsp()))
