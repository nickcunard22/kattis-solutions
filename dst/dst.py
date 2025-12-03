n = int(input())
for i in range(n):
    line = input().split()
    forward = line.pop(0) == 'F'
    f = 1 if forward else -1

    line = tuple(map(int, line))
    d, h, m = line

    m += f * d

    if m >= 60 or m < 0:
        h += m // 60
        m %= 60

    if h >= 24 or h < 0:
        h %= 24
    
    print(h, m)
