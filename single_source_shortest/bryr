import heapq
from math import inf

n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((c, b))
    adj[b].append((c, a))

q = [(0, 1)] # weight 0 location 1
min_weight = 0
best = inf
visited = set()

while q:
    current_weight, node = heapq.heappop(q)
    if node in visited:
        continue

    visited.add(node)

    if node == n:
        best = min(current_weight, best)

    for weight, neighbor in adj[node]:
        heapq.heappush(q, (weight + current_weight, neighbor))

print(best)
