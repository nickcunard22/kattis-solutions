import heapq
import sys
from math import inf

while True:
    n, m, q, s = tuple(map(int, input().split()))
    if (n, m, q, s) == (0, 0, 0, 0):
        break

    adj = [[] for _ in range(n)]

    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((w, v)) # directed graph
        # adj[v].append((w, u))

    # RUN DJIKSTRAS
    heap = [(0, s)]
    distances = [inf for _ in range(n)] # store all the best dists
    best = inf
    visited = set()

    while heap:
        current_weight, node = heapq.heappop(heap)

        distances[node] = min(current_weight, distances[node])
        
        if node in visited:
            continue
        visited.add(node)

        for weight, neighbor in adj[node]:
            heapq.heappush(heap, (weight + current_weight, neighbor))

    # QUERY OUTPUT
    for _ in range(q):
        end = int(input())
        print(distances[end] if distances[end] != inf else "Impossible")
