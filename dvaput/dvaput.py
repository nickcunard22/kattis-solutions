import sys

l = int(input())
string = sys.stdin.readline()

string += '$'
n = len(string)

# sa contains the offsets of each suffix
sa = [i for i in range(n)]

# rank contains the rank (rank1, rank2) of each suffix
rank = [(ord(string[i]), 0) for i in range(n)] # store first string char initially

def counting_sort(sa, n, key):
    max_val = max(key(i) for i in range(n))
    count = [0] * (max_val + 1)
    for i in range(n):
        count[key(i)] += 1
    pos = [0] * (max_val + 1)
    for i in range(1, max_val + 1):
        pos[i] = pos[i-1] + count[i-1]
    result = [0] * n
    for i in sa:
        k = key(i)
        result[pos[k]] = i
        pos[k] += 1
    return result

# construct sa
k = 1
while k < n: # double

    # update secondary ranks according to what we've already computed
    for i in range(n):
        rank[i] = (rank[i][0], rank[i + k][0]) if i + k < n else (rank[i][0], 0)

    # sort suffix array based on computed ranks using radix sort
    sa = counting_sort(sa, n, lambda i: rank[i][1])
    sa = counting_sort(sa, n, lambda i: rank[i][0])

    new_rank = [0] * n
    r = 0
    new_rank[sa[0]] = 0

    # assign ranks to each suffix
    for i in range(1, n):
        if rank[sa[i]] == rank[sa[i-1]]: # if pair is same, assign same rank
            new_rank[sa[i]] = r
        else: # otherwise assign new rank!
            r += 1
            new_rank[sa[i]] = r

    for i in range(n):
        rank[i] = (new_rank[i], 0)

    if r == n - 1:
        break
    
    k *= 2

def compute_lcp(s, sa):
    n = len(s)
    # rank[i] is the position of suffix s[i:] in the sorted sa
    rank = [0] * n
    for i in range(n):
        rank[sa[i]] = i

    lcp = [0] * n
    h = 0

    for i in range(n):
        if rank[i] > 0:
            # j is the index of the suffix that comes before suffix i in sa
            j = sa[rank[i] - 1]
            
            # While the characters match, increment the common length
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            
            lcp[rank[i]] = h
            
            # will have at least h-1 characters in common
            if h > 0:
                h -= 1
            
    return lcp


lcp = compute_lcp(string, sa)

print(max(lcp))