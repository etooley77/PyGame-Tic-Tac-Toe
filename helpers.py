

# Check the board for a win
def check_win(pieces, color, player):
    if len(pieces) >= 3:
        for i in range(len(pieces)):
            # Check from tile zero
            if pieces[i] == 0:
                # Check for a win in a row
                if pieces[i] + 1 in pieces and pieces[i] + 2 in pieces:
                    player.score += 1
                    return [True, color]
                # Check for a win in a column
                if pieces[i] + 3 in pieces and pieces[i] + 6 in pieces:
                    player.score += 1
                    return [True, color]
                # Check for a win in a diagonal
                if pieces[i] + 4 in pieces and pieces[i] + 8 in pieces:
                    player.score += 1
                    return [True, color]
            
            # Check from tile 3
            elif pieces[i] == 3:
                # Check for a win in a row
                if pieces[i] + 1 in pieces and pieces[i] + 2 in pieces:
                    player.score += 1
                    return [True, color]
                
            # Check from tile 6
            elif pieces[i] == 6:
                # Check for a win in a row
                if pieces[i] + 1 in pieces and pieces[i] + 2 in pieces:
                    player.score += 1
                    return [True, color]
                # Check for a win in a diagonal
                if pieces[i] - 2 in pieces and pieces[i] - 4 in pieces:
                    player.score += 1
                    return [True, color]
                
            # Check from tile 1
            elif pieces[i] == 1:
                # Check for a win in a column
                if pieces[i] + 3 in pieces and pieces[i] + 6 in pieces:
                    player.score += 1
                    return [True, color]
                
            # Check from tile 2
            elif pieces[i] == 2:
                # Check for a win in a column
                if pieces[i] + 3 in pieces and pieces[i] + 6 in pieces:
                    player.score += 1
                    return [True, color]
                
        return [False, ""]
    return [False, ""]

def check_tie(board):
    curr_board = board[:-1]
    check_board = []

    for tile in curr_board:
        if tile == 'r' or tile == 'b':
            check_board.append("x")
        else:
            check_board.append("_")

    if check_board == ["x", "x", "x", "x", "x", "x", "x", "x", "x"]:
        return [True, "Nobody"]
    return [False, ""]