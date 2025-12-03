'''
given all pokemon, find the
kth many with highest ad, de, and hp
there will be some overlap (pokemon with highest of two stats)
'''

n, k = map(int, input().split())

team = set()

all_pokemon = {i: tuple(map(int, input().split())) for i in range(n)}
attack = dict(sorted(all_pokemon.items(), key=lambda x: -x[1][0]))
defense = dict(sorted(all_pokemon.items(), key=lambda x: -x[1][1]))
hp = dict(sorted(all_pokemon.items(), key=lambda x: -x[1][2]))

team.update(list(attack.keys())[:k])
team.update(list(defense.keys())[:k])
team.update(list(hp.keys())[:k])

print(len(team))