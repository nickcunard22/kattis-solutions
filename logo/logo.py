from math import sin, cos, dist, radians

test_cases = int(input())
for _ in range(test_cases):
    commands = int(input())
    x = y = direction = 0
    for _ in range(commands):
        command, val = input().split()
        val = int(val)

        if command == 'fd':
            dx = cos(radians(direction)) * val
            dy = sin(radians(direction)) * val
            x += dx
            y += dy
        elif command == 'lt':
            direction -= val
            direction %= 360
        elif command == 'rt':
            direction += val 
            direction %= 360
        elif command == 'bk':
            dx = cos(radians(direction)) * val
            dy = sin(radians(direction)) * val
            x -= dx
            y -= dy
        
    print(round(dist((x, y), (0, 0))))
