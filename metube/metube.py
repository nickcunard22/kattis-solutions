from copy import deepcopy

num_videos = int(input())
all_categories = set()

encode = lambda s: "".join(sorted(s))
decode = lambda s: set(s)

dp = {}
dp[""] = 0
for _ in range(num_videos):
    length, categories = input().split()
    length = int(length)
    categories = set(categories)

    all_categories = all_categories.union(categories)

    for prev_categories, time_watched in deepcopy(dp).items():
        key = encode(decode(prev_categories).union(categories))
        if key in dp.keys():
            dp[key] = min(length + time_watched, dp[key])
        else:
            dp[key] = length + time_watched


print(dp[encode(all_categories)])