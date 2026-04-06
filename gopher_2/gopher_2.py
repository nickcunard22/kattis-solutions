from sys import stdin

n, m, s, v = map(int, input().split())

# gophers
gophers = [tuple(map(float, input().split())) for _ in range(n)]

# holes
holes = [tuple(map(float, input().split())) for _ in range(m)]

print(gophers, holes)
