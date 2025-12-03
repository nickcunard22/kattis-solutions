from copy import deepcopy

def solve(nums, N):
    #dp[sum] = one way to reach this sum (as a bit vector)
    dp = {}
    dp[0] = 0

    for i, num in enumerate(nums):
        # check against all previously computed sums
        for sum, v in deepcopy(dp).items():
            nv = v
            nv |= (1 << i)
            
            # check if new sum has already been found
            if num + sum in dp.keys():
                return dp[num + sum], nv # return existing set, new set

            # add new set to dp
            dp[sum + num] = nv

T = int(input())
for case in range(T):
    nums = list(map(int, input().split()))
    N = nums.pop(0)

    v1, v2 = solve(nums, N)
    print(f'Case #{case + 1}:')
    for i in range(N):
        bit = (v1 >> i) & 1
        if bit:
            print(nums[i], end=' ')
    print()
    for i in range(N):
        bit = (v2 >> i) & 1
        if bit:
            print(nums[i], end=' ')
    print()