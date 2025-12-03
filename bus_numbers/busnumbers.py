input()
nums = list(map(int, input().split()))

nums.sort()

i = 0
j = 1
while i < len(nums):
    if j < len(nums) and nums[i] == nums[j] - 1:
        lo = nums[i]
        while j < len(nums) and nums[i] == nums[j] - 1:
            i += 1
            j += 1 
        if nums[i] - lo >= 2:
            print(f"{lo}-{nums[i]} ", end='')
        else:
            print(f"{lo} {nums[i]} ", end='')
    else:
        print(f"{nums[i]} ", end='')
    i += 1
    j += 1
print()