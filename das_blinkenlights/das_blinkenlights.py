def gcd(a, b):
    while (r := a % b) != 0:
        a, b = b, r
    return b

def lcm(a, b):
    return a * b // gcd(a, b)

p, q, s = map(int, input().split())

if q > p:
    p, q = q, p

print('yes' if lcm(p, q) <= s else 'no')