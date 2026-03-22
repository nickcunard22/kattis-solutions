
while True:
    num_vertices, num_edges = map(int, input().split())
    if (num_vertices, num_edges) == (0, 0):
        break

    graph = [[] for _ in range(num_vertices + 1)] # adj list

    for _ in range(num_edges):
        u, v = map(int, input().split())

        graph[u].append(v)

    
    in_degrees = [0] * (num_vertices + 1)
    for u in range(num_vertices + 1):
        for v in graph[u]:
            in_degrees[v] += 1

    start_v = None
    end_count = 0
    valid = True
    circuit_start = None

    for u in range(num_vertices + 1):
        out_d = len(graph[u])
        in_d = in_degrees[u]
        diff = out_d - in_d
        if diff == 1:
            if start_v is not None:
                valid = False; break
            start_v = u
        elif diff == -1:
            end_count += 1
            if end_count > 1:
                valid = False; break
        elif diff != 0:
            valid = False; break
        if out_d > 0 and circuit_start is None:
            circuit_start = u

    if start_v is not None and end_count != 1:
        valid = False

    if not valid:
        print("Impossible")
        continue

    if start_v is None:
        start_v = circuit_start

    if start_v is None:
        print("Impossible")
        continue

    # hierholzer
    path = []
    st = [start_v]
    while st:
        v = st[-1]
        if len(graph[v]) == 0:
            path.append(v)
            st.pop()
        else:
            neighbor = graph[v].pop()
            st.append(neighbor)

    if len(path) == num_edges + 1:
        print(' '.join(map(str, reversed(path))))
    else:
        print("Impossible")
    
