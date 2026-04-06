from math import lcm, ceil
from fractions import Fraction

def egcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x1, y1 = egcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return d, x, y

# read in input as fractions
c, a, b = tuple(map(Fraction, input().split()))

# compute lcm of denominators
m = lcm(a.denominator, b.denominator, c.denominator)

# multiply by lcm (to get all integer equation)
a, b, c = int(a * m), int(b * m), int(c * m)

# compute extended gcd
d, x, y = egcd(a, b)

# ax + by = d
assert a * x + b * y == d

# axc + byc = c
x1 = x * (c // d)
y1 = y * (c // d)

A, B = a // d, b // d

# check values of n s.t. y1 + n * A >= 0 and x1 - n * B >= 0
n_min = ceil(-x1 / B)
n_max = y1 // A

if n_min > n_max:
    print("none")
else:
    for n in range(n_min, n_max + 1):
        xn = x1 + B * n
        yn = y1 - A * n
        print(xn, yn)
