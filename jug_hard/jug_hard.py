def gcd(a, b):
    while (r := a % b) != 0:
        a, b = b, r
    return b

T = int(input())
for _ in range(T):
    a, b, d = map(int, input().split())
    if d % gcd(a, b) == 0:
        print('Yes')
    else:
        print('No')