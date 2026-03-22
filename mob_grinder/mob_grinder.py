'''
observations:
    never want up tiles on the top row,
    right on right side, etc.
    
brute-force backtracking approach:
    try placing each of the four types of conveyors
    move on to the next square with n - 1 conveyors
    try all possibilities via backtracking
    O(slow as fuck)

validation function:    
    start at square i,j 
    go to square it points to repeatedly
    if we detect a cycle, it fails
    if we reach end, compress all squares along the way
a valid mob grinder can be thought of as a union-find data structure,
where every node points to the * (!)

what if we go backwards?
    start at *
    dfs, randomly placing VALID conveyors
    backtrack when they fail
'''

grinders = int(input())

def neighbors(i, j, u, r, d, l):
    neighbors = []
    if i-1 >= 0 and grid[i-1][j] == '' and d > 0: neighbors.append((i-1, j, 'D'))
    if i+1 <  n and grid[i+1][j] == '' and u > 0: neighbors.append((i+1, j, 'U'))
    if j-1 >= 0 and grid[i][j-1] == '' and r > 0: neighbors.append((i, j-1, 'R'))
    if j+1 <  m and grid[i][j+1] == '' and l > 0: neighbors.append((i, j+1, 'L'))
    return neighbors

def mrv(frontier, u, r, d, l_left):
    best_cell = None
    best_cands = None
    for cell in frontier:
        cands = neighbors(cell[0], cell[1], u, r, d, l_left)
        if best_cands is None or len(cands) < len(best_cands):
            best_cell, best_cands = cell, cands
            if len(best_cands) <= 1:  # early exit on 0/1 options
                break
    return best_cell, best_cands

for it in range(grinders):
    # n many rows, m many cols
    n, m, u, r, d, l = map(int, input().split())

    grid = [['' for _ in range(m)] for _ in range(n)]
    grid[0][m - 1] = '*'
    
    # frontier is a set of all the squares currently in our path
    # we use it to 
    def dfs(frontier, u, r, d, l):

        # base cases
        if u == r == d == l == 0:
            return True
        if not frontier:
            return False

        # find the child with the fewest number of possibilities and begin search there
        (i, j), cand = mrv(frontier, u, r, d, l)

        # try attaching children
        for ni, nj, ch in cand:
            grid[ni][nj] = ch
            frontier.add((ni, nj))
            u2, r2, d2, l2 = u, r, d, l
            if   ch == 'U': u2 -= 1
            elif ch == 'R': r2 -= 1
            elif ch == 'D': d2 -= 1
            else:           l2 -= 1

            if dfs(frontier, u2, r2, d2, l2):
                return True

            frontier.remove((ni, nj))
            grid[ni][nj] = ''

        # try not attaching children
        frontier.remove((i, j))
        if dfs(frontier, u, r, d, l):
            return True

        frontier.add((i, j))
        return False

    if dfs(set([(0, m - 1)]), u, r, d, l):
        for row in grid:
            print(''.join(row))
    else:
        print('impossible')
    if it != grinders - 1: # fencepost
        print()