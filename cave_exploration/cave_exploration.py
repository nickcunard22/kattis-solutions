def dfs(i, depth):
    global adj, depths, c, seen, parent, safe

    seen[i] = True
    depths[i] = depth
    c[i] = depth
    safe[i] = 1

    for neighbor in adj[i]:
        if seen[neighbor]: # seen neighbor already, this is a backedge
            if neighbor != parent[i]:
                c[i] = min(c[i], depths[neighbor]) # update i's ceiling accordingly
        else: # not seen
            parent[neighbor] = i
            dfs(neighbor, depth + 1)
            if c[neighbor] > depths[i]: # bridge: don't count neighbor's subtree
                safe[i] -= safe[neighbor]
            c[i] = min(c[i], c[neighbor])
            safe[i] += safe[neighbor]


N, M = map(int, input().split())

adj = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())

    adj[u].append(v)
    adj[v].append(u)

depths = [None for _ in range(N)]
c = [None for _ in range(N)]
parent = [None for _ in range(N)]
seen = [False for _ in range(N)]
safe = [0 for _ in range(N)]

dfs(0, 0)
print(safe[0])