'''
K * X is a fair distribution
need one extra candy:
K * X + 1

10 kids
7 candies per bag
20 kids = 21 candies

n * K + 1 = X * C
            ^

X = (n * K + 1) / C

n * K + 1 = 0 (mod C)

n = -1 * K^-1 (mod C)

'''

from math import gcd

def extended_euclidean(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, x1, y1 = extended_euclidean(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return g, x, y
    

t = int(input())
for _ in range(t):
    K, C = map(int, input().split())

    if gcd(K, C) == 1:
        _, k_inv, _ = extended_euclidean(K, C) # find -Kinv mod C
        n = (-k_inv) % C
        if n == 0: # n must be a positive natural number
            n = C
        X = (n * K + 1) // C
        print(X if X <= 10e9 else 'IMPOSSIBLE')
    else:
        print('IMPOSSIBLE')