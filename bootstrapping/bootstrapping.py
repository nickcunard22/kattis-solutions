'''
compute inverse of x^X

starting range: 1-10
bc n < 10^10
'''

from math import log
n = int(input())

x = 3
up = 10
lo = 1
while up - lo > 1e-6:
    if x ** x > n:
        up = x
    else:
        lo = x
    x = lo + (up - lo) / 2
print(x)
