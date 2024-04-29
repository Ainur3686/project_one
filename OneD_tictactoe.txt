#Step1. Write a function evaluate that accepts the string with the board as argument, returns one character 
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