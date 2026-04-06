from math import isqrt

n, q = map(int, input().split())

if n < 2:
    print(0)
    for _ in range(q):
        print(0)
else:
    limit = isqrt(n)
    seg_size = max(limit, 1)

    # Small sieve up to sqrt(n)
    small = bytearray(b'\x01') * (limit + 1)
    small[0] = small[1] = 0
    for i in range(2, isqrt(limit) + 1):
        if small[i]:
            for j in range(i * i, limit + 1, i):
                small[j] = 0
    small_primes = [i for i in range(2, limit + 1) if small[i]]

    primes = set()
    for l in range(0, n + 1, seg_size):
        r = min(l + seg_size, n + 1)
        seg = bytearray(b'\x01') * (r - l)

        if l == 0:
            if r > 0:
                seg[0] = 0
            if r > 1:
                seg[1] = 0

        for p in small_primes:
            start = max(p * p, ((l + p - 1) // p) * p) - l
            if start < 0:
                start += p
            for j in range(start, r - l, p):
                seg[j] = 0

        for i in range(r - l):
            if seg[i]:
                primes.add(l + i)

    print(len(primes))
    for _ in range(q):
        print(1 if int(input()) in primes else 0)
