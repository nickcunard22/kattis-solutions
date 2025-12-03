import heapq
n,k=map(int,input().split())
all_pokemon={i:tuple(map(int,input().split())) for i in range(n)}
print(len({tuple(heapq.nlargest(k, all_pokemon.items(),lambda x:x[1][i]))for i in range(3)}))