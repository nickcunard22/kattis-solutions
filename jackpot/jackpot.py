def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

assert lcm(10, 6) == 30
assert lcm(30, 15) == 30

n = int(input())

for _ in range(n):
    w = int(input())

    machines = list(map(int, input().split()))
    periodicity = machines[0]
    for p in machines[1:]:
        periodicity = lcm(periodicity, p)
        
    if periodicity > 1e9:
        print("More than a billion.")
    else:
        print(periodicity)