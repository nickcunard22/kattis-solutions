from math import gcd

n = int(input())
for _ in range(n):
    w, x, p_11, p_12 = tuple(map(int, input().split()))
    y, z, p_21, p_22 = tuple(map(int, input().split()))
    # solvable iff P = gcd(p_ij...) and s_ij mod p is also solvable

    p = gcd(p_11, p_12, p_21, p_22)
    
    w %= p; x %= p; y %= p; z %= p

