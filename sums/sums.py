T = int(input())

for _ in range(T):
    n = int(input())
    for i in range(n // 2 + 1, 0, -1):
        sum = val = i
        vals = []
        while val <= n:
            if val == n:
                print(n, vals, 'ok')
                break

            vals.append(val)
            val += 1
            sum += val

