from math import sin, cos, radians, dist
from statistics import mean

n = int(input())
while n != 0:
    locations = []
    for _ in range(n):
        line = input().split()
        x, y = list(map(float, line[0:2]))
        direction = float(line[3])

        for i in range(4, len(line), 2):
            if line[i] == 'walk':
                distance = float(line[i + 1])

                y += sin(radians(direction)) * distance
                x += cos(radians(direction)) * distance
            elif line[i] == 'turn':
                direction += float(line[i + 1])

        locations.append((x, y))
        # print(f'suggested location {x, y}')

    avg_x, avg_y = mean([l[0] for l in locations]), mean([l[1] for l in locations])
    
    locations.sort(key=lambda l: dist((avg_x, avg_y), l))

    print(avg_x, avg_y, dist(locations[-1], (avg_x, avg_y)))

    n = int(input())
