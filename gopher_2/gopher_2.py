from sys import stdin
from math import dist

while True:
    try:
        n, m, s, v = map(int, input().split())
    except EOFError:
        break

    gophers = [tuple(map(float, input().split())) for _ in range(n)]

    holes = [tuple(map(float, input().split())) for _ in range(m)]

    graph = [[] for _ in range(n)] # maps gopher -> hole

    for i, gopher in enumerate(gophers):
        for j, hole in enumerate(holes):
            if dist(gopher, hole) < v * s: # if goph can make it
                graph[i].append(j) # add new edge from i -> j

    # hungarian
    def dfs(u, visited, matching):
        ''' brute force dfs, return true if augmenting path exists '''
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
            
                # if v is unmatched, or future neighbor is unmatched
                if matching[v] == -1 or dfs(matching[v], visited, matching):
                    matching[v] = u
                    return True
                
        return False

    matching = [-1] * m # hole -> gopher

    for i in range(n):
        dfs(i, [False] * m, matching)

    print(matching.count(-1))
