from math import inf

# Disjoint set data structure
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.rank[s1] < self.rank[s2]:
                self.parent[s1] = s2
            elif self.rank[s1] > self.rank[s2]:
                self.parent[s2] = s1
            else:
                self.parent[s2] = s1
                self.rank[s1] += 1

N = int(input())
A = list(map(int, input().split()))

dsu = DSU(N) # disjoint set will have N - 1 edges
cost = count = 0

edges = [(i, j) for i in range(len(A)) for j in range(len(A))]
edges.sort(key=lambda t: A[t[0]] + A[t[1]])

for i, j in edges:
    if dsu.find(i) != dsu.find(j): # does not create cycle
        dsu.union(i, j)
        cost += A[i] + A[j]
        count += 1
        if count == N - 1:
            break

print(cost)
