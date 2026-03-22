# if there is a bridge, print yes
# if the graph isnt already connected, print yes

def dfs(i, depth):
    global adj, depths, c, seen, has_bridge, parent

    seen[i] = True
    depths[i] = depth
    c[i] = depth

    for neighbor in adj[i]:
        if seen[neighbor]: # seen neighbor already, this is a backedge
            if neighbor != parent[i]:
                c[i] = min(c[i], depths[neighbor]) # update i's ceiling accordingly
        else: # not seen
            parent[neighbor] = i
            dfs(neighbor, depth + 1)
            if c[neighbor] > depths[i]: # bridge
                has_bridge = True
            c[i] = min(c[i], c[neighbor])

while True:
    p, c = tuple(map(int, input().split()))
    if (p, c) == (0, 0):
        break

    adj = [[] for _ in range(p)]
    for _ in range(c):
        a, b = tuple(map(int, input().split())) 
        assert a <= p
        assert b <= p

        adj[a].append(b)
        adj[b].append(a)

    depths = [None for _ in range(p)]
    c = [None for _ in range(p)]
    seen = [False for _ in range(p)]
    parent = [None for _ in range(p)]
    has_bridge = False

    dfs(0, 0)
    if not all(seen):
        print('Yes')
    else:
        print('Yes') if has_bridge else print('No')
    

