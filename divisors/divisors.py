from math import sqrt

n = int(input())
    
divisors = set()

for i in range(1, int(sqrt(n)) + 1):
    q = n / i
    if int(q) == q:
        divisors.add(i)
        divisors.add(int(q))

divisors = list(divisors)
divisors.sort()
for d in divisors:
    print(d)