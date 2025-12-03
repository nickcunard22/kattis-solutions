import math

r = int(input())

points = 0
for x in range(r):
    y = math.sqrt((r ** 2) - (x ** 2))
    points += math.floor(y)
points *= 4
points += 1

print(points)