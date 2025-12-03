num_cards = int(input())

cards = list(map(int, input().split()))
cards.sort()

num_ranges = int(input())

ranges = [tuple(map(int, input().split())) for _ in range(num_ranges)]

def binary_search(val):
    lo = 0 
    hi = num_cards - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if cards[mid] == val:
            return mid
        if cards[mid] < val:
            lo = mid + 1
        else:
            hi = mid - 1
    return mid

for range in ranges:
    l, r = range

    # print(binary_search(l), binary_search(r))

    cards_in_range = binary_search(r) - binary_search(l)
    print(cards_in_range)
