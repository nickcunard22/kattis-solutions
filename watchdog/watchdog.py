import math

def find_leash():
    for i in range(S):
        for j in range(S):
            radius = min(min(S - i, S - j), min(i, j))
            if (i, j) in hatches:
                continue

            for hatch in hatches:
                if math.dist((i, j), hatch) > radius: # if hatch not in circle
                    break
            else:
                return f'{i} {j}' 
            
    return 'poodle'

N = int(input())
for _ in range(N):
    S, H = map(int, input().split())

    hatches = [tuple(map(int, input().split())) for _ in range(H)]
    
    print(find_leash())
