from sys import stdin

def gcd(a, b):
    while (r := a % b) != 0:
        a, b = b, r
    return b

def lcm(a, b):
    return a * b // gcd(a, b)

for line in stdin.readlines():
    l = 1
    for num in list(map(int, line.split())):
        l = lcm(l, num)
    print(l)