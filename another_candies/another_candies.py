T = int(input())
for _ in range(T):
    input()
    num_children = int(input())

    total_candies = 0
    for _ in range(num_children):
        total_candies += int(input())

    if total_candies % num_children == 0:
        print('YES')
    else:
        print('NO')
