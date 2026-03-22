r, c = tuple(map(int, input().split()))

grid = [input() for _ in range(r)]
seen = [[False for _ in range(c)] for _ in range(r)]

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def dfs(i, j):
    for ni, nj in DIRECTIONS:
        if 0 <= i + ni < r and 0 <= j + nj < c and not seen[i + ni][j + nj] and \
            (grid[i + ni][j + nj] == 'L' or grid[i + ni][j + nj] == 'C'): 
            
            seen[i + ni][j + nj] = True
            dfs(i + ni, j + nj)

count = 0

for i in range(r):
    for j in range(c):
        if grid[i][j] == 'L' and not seen[i][j]:
            dfs(i, j)
            count += 1

print(count)