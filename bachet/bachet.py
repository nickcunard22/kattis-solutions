while True:
    try:
        line = input().split()
    except EOFError:
        break

    n = int(line[0])
    moves = sorted(map(int, line[2:]))

    '''
    dp[i] = 1 means the current player wins with i many stones remaining
    dp[i] = -1 means the other player wins with i many stones remaining
    to check if you win by making a move m, flip the value at dp[i - m]
    '''
    dp = [0] * (n + 1)
    dp[0] = -1
    dp[1] = 1

    for i in range(2, n + 1, 1):
        dp[i] = -1
        for move in moves:
            if move > i: # skip invalid moves
                break # sorted, skip the rest of the moves here
            # try move
            winner = -1 * dp[i - move]
            if winner == 1: # found a winning move
                dp[i] = 1
                break
    
    if dp[n] == 1:
        print("Stan wins")
    else:
        print("Ollie wins")