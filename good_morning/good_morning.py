from math import inf

KEYBOARD = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [None, 0, None]]

def dfs(i, j, val: str, target: int):
    # print(i, j, val, target)
    right = down = press = None
        
    # mapping val string -> difference value
    # basically: how close is the current string?
    diff = lambda v: abs(target - int(v)) if v else target

    if val and diff(val) == 0:
        return val
    
    # go right
    if j + 1 < 3 and KEYBOARD[i][j + 1] is not None:
        right = dfs(i, j + 1, val, target)
    # go down 
    if i + 1 < 4 and KEYBOARD[i + 1][j] is not None:
        down = dfs(i + 1, j, val, target)
    # press
    if diff(val + str(KEYBOARD[i][j])) < diff(val): # if pressing doesn't cause more error
        press = dfs(i, j, val + str(KEYBOARD[i][j]), target)        
    
    return min([right, down, press, val], key=diff)                                                        


T = int(input())

for _ in range(T):
    k = int(input())

    print(dfs(0, 0, '', k))
