from math import inf
n = int(input())
min_y = inf
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 < 0 and x2 < 0) or (x1 > 0 and x2 > 0):
        continue
    m = (y2 - y1) / (x2 - x1)
    y = m * -x1 + y1
    if y >= 0:
        min_y = min(min_y, y)
print(min_y if min_y != inf else -1.0)