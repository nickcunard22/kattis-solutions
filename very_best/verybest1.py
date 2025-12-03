import heapq
n, k = map(int, input().split())
team = set()
all_pokemon = {i: tuple(map(int, input().split())) for i in range(n)}
for i in range(3): 
    team.update(heapq.nlargest(k, all_pokemon.items(), key=lambda x: x[1][i]))
print(len(team))