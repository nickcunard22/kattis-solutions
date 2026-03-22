'''
a b c 
d e f
g h i

where:
a * b * c = n
d * e * f = n
g * h * i = n
a * e * i = n
g * e * c = n
'''
square = [[-1 for _ in range(3)] for _ in range(3)]

def constraints(i, j):
    # compute constraints for this square
    # return a maximum value (min is always 1)
    row_product = 1
    for val in square[i]:
        if square != -1:
            row_product *= val
    col_product = 1
    for row in square:
        if row[j] != -1:
            col_product *= row[j]
    if i + j == 3: # 2,0 1,1 0,1 diagonal
        up_diag_product = 1
    if i == j: # 0,0 1,1 2,2 diagonal 
        down_diag_product = 1 


def num_magic_squares(n):
    # assign value between 1 and n
    # update constraints accordingly
    # forward check to see if this fails
    #   if fails, try another number (maybe binary search?)
    #   if successful, keep going until failure
    # backtrack 
    for i in range(3):
        for j in range(3):
            square[i][j] = 

t = int(input())
for _ in range(t):
    n = int(input())
    print(num_magic_squares(n))
