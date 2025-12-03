n = int(input())

for _ in range(n):
    num = int(input())
    max_bits = 0
    while num:
        bin_rep = bin(num)
        c = 0
        for bit in bin_rep:
            if bit == '1':
                c += 1
        max_bits = max(max_bits, c)
        num //= 10
    print(max_bits)
