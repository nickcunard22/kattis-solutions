from math import inf

N = int(input())

# tile can be either ?, S (saw), or . (nothing)
# when mario reaches a saw: fire -> super, super -> small, small -> death
# questions you can *choose* to upgrade him
# small mario takes 1 game tick per tile
# big marios take 2 game ticks per tile
level = input()

# 3xN matrix
# row index i determines which form mario is in (0=small, 1=super, 2-fire)
# col index j is fastest way to get to this square such that mario is currently in this form 
dp = [[-1 for _ in range(N)] for _ in range(3)]
dp[0][0] = 0
dp[1][0] = 0
dp[2][0] = 0

for j in range(1, N):
    tile = level[j]
    if tile == '.':
        dp[0][j] = dp[0][j - 1] + 1 if dp[0][j - 1] != -1 else -1
        dp[1][j] = dp[1][j - 1] + 2 if dp[1][j - 1] != -1 else -1
        dp[2][j] = dp[2][j - 1] + 2 if dp[2][j - 1] != -1 else -1
    elif tile == 'S':
        # small mario DIES
        dp[0][j] = dp[1][j - 1] + 2 if dp[1][j - 1] != -1 else -1 # super -> small
        dp[1][j] = dp[2][j - 1] + 2 if dp[2][j - 1] != -1 else -1 # fire -> super
    elif tile == '?':
        dp[0][j] = dp[0][j - 1] + 1 if dp[0][j - 1] != -1 else -1

        options = []
        if dp[1][j - 1] != -1:
            options.append(dp[1][j - 1] + 2)  # was super, didn't activate, moved 2 ticks
        if dp[0][j - 1] != -1:
            options.append(dp[0][j - 1] + 1)  # was small, activated, moved 1 tick
        dp[1][j] = min(options) if options else -1

        options = []
        if dp[2][j - 1] != -1:
            options.append(dp[2][j - 1] + 2)  # was fire, moved 2 ticks
        if dp[1][j - 1] != -1:
            options.append(dp[1][j - 1] + 2)  # was super, activated, moved 2 ticks
        dp[2][j] = min(options) if options else -1
    else:
        print('what')

print(dp)
speeds = [dp[j][N - 1] for j in range(3) if dp[j][N - 1] != -1]
print(min(speeds) if speeds else -1)