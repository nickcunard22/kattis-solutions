start = tuple(map(int, input().split()))
end = tuple(map(int, input().split()))
 
n = int(input())

adj = [[] for _ in range(n + 2)]

for i in range(n):
    cannon = tuple(map(int, input().split()))
    adj[i]