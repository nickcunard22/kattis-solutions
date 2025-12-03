from heapq import heappush, heappop
from math import inf

N = int(input())
fees = [int(input()) for _ in range(N)]

# PQ items are (cost_so_far, square, prev_jump)
pq = []
heappush(pq, (0, 0, 0))

# best[(square, prev_jump)] = min cost to reach that exact state
best = {(0, 0): 0}

while pq:
    cost, square, prev_jump = heappop(pq)

    # If this state is already dominated, skip
    if cost != best.get((square, prev_jump), inf):
        continue

    # Goal: the first time we pop N-1, this is optimal
    if square == N - 1:
        print(cost)
        break

    jump = prev_jump + 1

    # forward
    ns = square + jump
    if ns < N:
        nc = cost + fees[ns]
        if nc < best.get((ns, jump), inf):
            best[(ns, jump)] = nc
            heappush(pq, (nc, ns, jump))

    # backward (use current jump length)
    ns = square - prev_jump
    if ns >= 0:
        nc = cost + fees[ns]
        if nc < best.get((ns, prev_jump), inf):
            best[(ns, prev_jump)] = nc
            heappush(pq, (nc, ns, prev_jump))
else:
    # If loop exits normally, destination is unreachable
    print(inf)
