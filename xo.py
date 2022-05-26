import os
from random import randint
# board structure is made with a dict, index from 1 to 9 indicating positions on the board
# all positions are intialized empty
board = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}

# ai playes with X "maximizing"
# player playes with O "minimizing"
ai = "X"
player = "O"

# function to draw the board
def drawBoard(board):
    for key in board:
        if key % 3 == 0:
            print(board[key] + "\n")
        else:
            print(board[key] + " | ", end="")


# functions to check if a position is empty or no
def isEmpty(pos):
    if board[pos] == " ":
        return True
    else:
        return False


# function to check if it is a draw
def checkDraw():
    for key in board:
        if board[key] == " ":
            return False
    return True


# function to check for win, it returns a dict i.e. {0: True, 1: 'X'}
# which means there is a win and 'X' is the winner
# index 0 True or False (win or no win), index 1 winner ('X' or 'O' or None)
def checkWin():
    if board[1] == board[2] and board[1] == board[3] and board[1] != " ":
        return {0: True, 1: board[1], 2: [1,2,3]}
    elif board[4] == board[5] and board[4] == board[6] and board[4] != " ":
        return {0: True, 1: board[4], 2: [4,5,6]}
    elif board[7] == board[8] and board[7] == board[9] and board[7] != " ":
        return {0: True, 1: board[7], 2: [7,8,9]}
    elif board[1] == board[4] and board[1] == board[7] and board[1] != " ":
        return {0: True, 1: board[1], 2: [1,4,7]}
    elif board[2] == board[5] and board[2] == board[8] and board[2] != " ":
        return {0: True, 1: board[2], 2: [2,5,8]}
    elif board[3] == board[6] and board[3] == board[9] and board[3] != " ":
        return {0: True, 1: board[3], 2: [3,6,9]}
    elif board[1] == board[5] and board[1] == board[9] and board[1] != " ":
        return {0: True, 1: board[1], 2: [1,5,9]}
    elif board[7] == board[5] and board[7] == board[3] and board[7] != " ":
        return {0: True, 1: board[7], 2: [7,5,3]}
    else:
        return {0: False, 1: None, 2: None}


# insert a letter 'X' or 'O' at position
def insertPos(letter, pos):
    if isEmpty(pos):
        board[pos] = letter
        os.system("clear")
        drawBoard(board)

        # check for win after inserting
        if checkWin()[0]:
            if checkWin()[1] == "X":
                print("Ai wins")
                # exit()
            else:
                print("player wins")
                # exit()
        if checkDraw():
            print("IT IS DRAW!")
            # exit()
        return
    else:  # if the provided position is not empty, re enter position
        print("position is not empty")
        pos = int(input("enter another position: "))
        insertPos(letter, pos)
        return


def minimax(board, depth, isMaximizing):
    if checkWin()[1] == ai:
        return 100
    elif checkWin()[1] == player:
        return -100
    elif checkDraw():
        return 0

    if isMaximizing:
        bestScore = -1000

        for key in board:
            if board[key] == " ":
                board[key] = ai
                score = int(minimax(board, 100, False))
                board[key] = " "
                if score > bestScore:
                    bestScore = score
        return bestScore

    else:
        bestScore = 1000

        for key in board:
            if board[key] == " ":
                board[key] = ai
                score = int(minimax(board, 100, True))
                board[key] = " "
                if score < bestScore:
                    bestScore = score
        return bestScore


def playerMove(pos):
    insertPos(player, pos)
    return
def getrand():
    return randint(1,9)    


def aiMove():
    bestScore = -1000
    bestMove = 0

    for key in board:
        if board[key] == " ":
            board[key] = ai
            score = int(minimax(board, 100, False))
            board[key] = " "
            if score > bestScore:
                bestScore = score
                bestMove = key

    insertPos(ai, bestMove)
    return bestMove


def start_game():
    while not checkWin()[0]:
        aiMove()
        playerMove()
