# Disjoint set data structure
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.size = [1] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.rank[s1] < self.rank[s2]:
                self.parent[s1] = s2
                self.size[s2] += self.size[s1]
            elif self.rank[s1] > self.rank[s2]:
                self.parent[s2] = s1
                self.size[s1] += self.size[s2]
            else:
                self.parent[s2] = s1
                self.rank[s1] += 1
                self.size[s1] += self.size[s2]

    def get_size(self, i):
        return self.size[self.find(i)]



R = int(input())
C = int(input())
U = int(input())

grid = []
s_loc = None

for x in range(R):
    row = input()
    grid.append(list(row))
    for y, c in enumerate(row):
        if c == 'S':
            s_loc = x, y
            s_loc_rolled = x * C + y
            break

DIRECTIONS = [[0, 1], [1, 0], [-1, 0], [0, -1]]

dsu = DSU(R * C)

for i in range(R):
    for j in range(C):
        if grid[i][j] in '#S':
            for DI, DJ in DIRECTIONS:
                ni, nj = i + DI, j + DJ
                if 0 <= ni < R and 0 <= nj < C and grid[ni][nj] in '#S':
                    dsu.union(i * C + j, ni * C + nj)
print(dsu.get_size(s_loc_rolled))

for _ in range(U):
    x, y = map(int, input().split())
    x -= 1
    y -= 1

    grid[x][y] = '#'
    for DI, DJ in DIRECTIONS:
        if 0 <= x + DI < R and 0 <= y + DJ < C and (grid[x + DI][y + DJ] == '#' or grid[x + DI][y + DJ] == 'S'):
            dsu.union(x*C + y, ((x+DI)*C) + (y+DJ))

    print(dsu.get_size(s_loc_rolled))


