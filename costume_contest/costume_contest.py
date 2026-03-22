from collections import defaultdict

N = int(input())

costumes = defaultdict(int)

for _ in range(N):
    line = input()
    costumes[line] += 1

costume_items = sorted(costumes.items(), key=lambda x: (x[1], x[0]))

min_val = costume_items[0][1]

for costume, val in costume_items:
    if val > min_val:
        break
    print(costume)
