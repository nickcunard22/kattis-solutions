from collections import deque, defaultdict

# Flood-fill from the current frontier through BOTH placed tiles and empties.
# Return:
#  - seen: all cells in the connected region that can eventually reach '*'
#  - slots: dict { empty_cell -> list of legal directions ('U','R','D','L') }
#           where "legal" means: placing that dir points INTO the seen region.
def reachable_and_slots(frontier, u, r, d, lft):
    seen = set(frontier)
    q = deque(frontier)
    slots = {}                      # {(i,j): ['U','D',...]}
    while q:
        i, j = q.popleft()
        for ni, nj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
            if 0 <= ni < n and 0 <= nj < m and (ni, nj) not in seen:
                # We can traverse through placed tiles too; only count empties as slots.
                seen.add((ni, nj))
                q.append((ni, nj))
    # For every empty cell in the connected blob, compute which orientations can point into it
    # (i.e., has a neighbor in 'seen' in that direction and count > 0)
    for (i, j) in seen:
        if grid[i][j] != '':
            continue
        opts = []
        if i-1 >= 0 and (i-1, j) in seen and d > 0: opts.append('D')  # above -> 'D' points down into (i-1,j)? (backward build)
        if i+1 <  n and (i+1, j) in seen and u > 0: opts.append('U')
        if j-1 >= 0 and (i, j-1) in seen and r > 0: opts.append('R')
        if j+1 <  m and (i, j+1) in seen and lft > 0: opts.append('L')
        slots[(i, j)] = opts
    return seen, slots

# Fast feasibility checks + unit propagation (forced moves).
# Returns updated (frontier,u,r,d,lft) or None if impossible.
def unit_propagate(frontier, u, r, d, lft):
    while True:
        seen, slots = reachable_and_slots(frontier, u, r, d, lft)

        # prune: total capacity
        cap_total = sum(1 for _ in slots)         # reachable empties
        if u + r + d + lft > cap_total:
            return None

        # prune: per-direction capacity (upper bounds)
        dir_cap = defaultdict(int)
        for opts in slots.values():
            for ch in opts:
                dir_cap[ch] += 1
        if u > dir_cap['U'] or r > dir_cap['R'] or d > dir_cap['D'] or lft > dir_cap['L']:
            return None

        # unit-prop: any cell with exactly ONE legal orientation must be placed now
        forced = [(cell, opts[0]) for cell, opts in slots.items() if len(opts) == 1]
        if not forced:
            return frontier, u, r, d, lft  # nothing forced; stop

        changed = False
        for (ci, cj), ch in forced:
            if grid[ci][cj] != '':
                continue
            # place forced tile
            grid[ci][cj] = ch
            frontier.add((ci, cj))
            if   ch == 'U': u -= 1
            elif ch == 'R': r -= 1
            elif ch == 'D': d -= 1
            else:           lft -= 1
            if min(u, r, d, lft) < 0:
                return None
            changed = True
        if not changed:
            return frontier, u, r, d, lft
        
grinders = int(input())

for it in range(grinders):
    # n many rows, m many cols
    n, m, u, r, d, l = map(int, input().split())

    grid = [['' for _ in range(m)] for _ in range(n)]
    grid[0][m - 1] = '*'
        
    def dfs(frontier, u, r, d, lft):
        # propagate/prune first
        state = unit_propagate(frontier, u, r, d, lft)
        if state is None:
            return False
        frontier, u, r, d, lft = state

        # success
        if u == r == d == lft == 0:
            return True
        if not frontier:
            return False

        # MRV on PARENT (keep parent in frontier for branching)
        def neighbors_parent(i, j, u, r, d, lft):
            out = []
            if i-1 >= 0 and grid[i-1][j] == '' and d > 0: out.append((i-1, j, 'D'))
            if i+1 <  n and grid[i+1][j] == '' and u > 0: out.append((i+1, j, 'U'))
            if j-1 >= 0 and grid[i][j-1] == '' and r > 0: out.append((i, j-1, 'R'))
            if j+1 <  m and grid[i][j+1] == '' and lft > 0: out.append((i, j+1, 'L'))
            return out

        best_cell = None
        best_cands = None
        for cell in frontier:
            cands = neighbors_parent(cell[0], cell[1], u, r, d, lft)
            if best_cands is None or len(cands) < len(best_cands):
                best_cell, best_cands = cell, cands
                if len(best_cands) <= 1:
                    break

        i, j = best_cell
        # try attach a child (order by tightest remaining dir first)
        order = sorted(best_cands, key=lambda t: {'U':u, 'R':r, 'D':d, 'L':lft}[t[2]])
        for ni, nj, ch in order:
            grid[ni][nj] = ch
            frontier.add((ni, nj))
            u2, r2, d2, l2 = u, r, d, lft
            if   ch == 'U': u2 -= 1
            elif ch == 'R': r2 -= 1
            elif ch == 'D': d2 -= 1
            else:           l2 -= 1
            if dfs(frontier, u2, r2, d2, l2):
                return True
            frontier.remove((ni, nj))
            grid[ni][nj] = ''

        # skip/close this parent
        frontier.remove((i, j))
        ok = dfs(frontier, u, r, d, lft)
        frontier.add((i, j))
        return ok

    if dfs(set([(0, m - 1)]), u, r, d, l):
        for row in grid:
            print(''.join(row))
    else:
        print('impossible')
    if it != grinders - 1: # fencepost
        print()
