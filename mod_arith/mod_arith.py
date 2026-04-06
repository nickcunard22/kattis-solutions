'''
b^-1 = b^(m-2) % m iff m is prime
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

while True:
    n, t = map(int, input().split())

    if n == t == 0:
        break

    for _ in range(t):
        x, op, y = input().split()
        x, y = int(x), int(y)

        match op:
            case '+':
                print( ((x % n) + (y % n)) % n )
            case '-':
                print( ((x % n) - (y % n)) % n )
            case '*':
                print( ((x % n) * (y % n)) % n )
            case '/':
                if gcd(y, n) == 1:
                    _, y_inv, _ = extended_euclidean(y, n)
                    print( ((x % n) * y_inv) % n )
                else:
                    print(-1)
