import math
from sys import maxsize

n = int(input())
cranes = [tuple(map(int, input().split())) for _ in range(n)]

'''
CSP:
assign to the tallest crane first (just assign its height) (sorting - nlogn)
then, for each crane after that, - O(n^2)
    calculate the largest jib it could hold (then round down)
        search every other crane - O(n)
    assign that to the crane then move down

actually, order doesn't matter.
don't sort, and just compute each jib independently
'''

jibs = [0] * n
for i, (x, y, h) in enumerate(cranes):
    # find nearest neighbor
    min_dist = maxsize
    for j, (xn, yn, hn) in enumerate(cranes): # for each neighbor
        if j == i: 
            continue
        if hn < h: # ignore shorter neighbors
            continue
        dist = math.sqrt((xn - x) ** 2 + (yn - y) ** 2)
        min_dist = min(min_dist, dist)

    jibs[i] = min(h, math.floor(min_dist))

for jib in jibs:
    print(jib)