N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

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

matching = [-1] * (N + 1) 

for i in range(1, N + 1):
    dfs(i, [False] * (N + 1), matching)

if -1 in matching[1:]:
    print('Impossible')
else:
    for target in matching[1:]:
        print(target)
