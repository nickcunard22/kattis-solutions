from math import inf

n, V = map(int, input().split())

largest = -inf
for i in range(n):
    dim = tuple(map(int, input().split()))
    v = dim[0] * dim[1] * dim[2]
    largest = max(largest, v)
    
d = largest - V
print(d)