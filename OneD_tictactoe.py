#Step1. Write a function 'evaluate' that accepts the string with the board as argument, returns one character 
def evaluate(board):
    #Returns the character based on the status of the game
    if "xxx" in board:
        return "x"
    elif "ooo" in board:
        return "o"
    elif "-" not in board:
        return "!"
    else:
        return "-"

#Step2. Write a 'move' function (accepts the string with the board, a position (0-19) and mark(x or o), returns a board)
def move(board, mark, position):
    #Returns the game board with the given mark in the given position
    #splicing the substring from 'start position' up to the 'position'
    #concatinating the 'mark'
    #concatinating the rest of the board, excluding the position of the 'mark'
    #updating the board
    board = board[0:position]+ mark + board[position + 1:]
    #returning the updated board
    return board