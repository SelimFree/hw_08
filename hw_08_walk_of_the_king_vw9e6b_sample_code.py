# Programm name: Professors sample source code
# 15 Nov, 2020  Made by Selim ALtayev, vw9e6b
# Modifications: fixed some bugs

# Input: w, s, d, a or x to quit
# Output: chess table
import random
import time
rows = 8
def printBoard(coordsOfKing):
    print("\n"*5)
    coordsOfKing = [rows - coordsOfKing[0], coordsOfKing[1] - 1] # coords -> index
    #lineLength = 33 # for 3 spaces ("|" plus 3 = 4, 8*4 + 1 "|") # it should be calculate
    oneCell = "|     " # please use 3,5,7 odd numbers of spaces
    lineLength = rows * len(oneCell) + 1
    
    line = lineLength * "-"
    board1 = []
    pipes = rows * oneCell + "|"
    for i in range(rows):
        if coordsOfKing[0] != i: # [0] row-coordinate, [1] column-coordinate
            board1.append(pipes)
        else:
            board1.append(coordsOfKing[1] * oneCell +\
            "|" + " "*((len(oneCell)-2)//2) + "K" + " "*((len(oneCell)-2)//2) +\
            (rows - coordsOfKing[1] ) * oneCell)
    for i in range(rows):
        print(line)     
        print(board1[i])
    print(line)         

def repeatSteps(steps):
    coordsOfKing = [1, 5]
    printBoard(coordsOfKing)
    for i in range(len(steps)):
        if steps[i].upper() == "A": # left
            if coordsOfKing[1] != 1: # should not step to negative!
                coordsOfKing[1] -= 1  #mistake
            printBoard(coordsOfKing)
        elif steps[i].upper() == "D": # right
            if coordsOfKing[1] != rows: # should not step from the table!
                coordsOfKing[1] += 1 #mistake
            printBoard(coordsOfKing)
        elif steps[i].upper() == "S": # down
            if coordsOfKing[0] != 1: # should not step to negative!
                coordsOfKing[0] -= 1 #mistake
            printBoard(coordsOfKing)
        elif steps[i].upper() == "W": # up
            if coordsOfKing[0] != rows: # should not step from the table!
                coordsOfKing[0] += 1 #mistake
            printBoard(coordsOfKing)  

        time.sleep(2)

def askTheUser(coordsOfKing):
    steps = []
    while True:
        step = input("Which direction the king should step? (ASDW / X / R) ")
        if step.upper() == "A": # left
            if coordsOfKing[1] != 1: # should not step to negative!
                coordsOfKing[1] -= 1  #mistake
            printBoard(coordsOfKing)
            steps.append(step)
        elif step.upper() == "D": # right
            if coordsOfKing[1] != rows: # should not step from the table!
                coordsOfKing[1] += 1 #mistake
            printBoard(coordsOfKing)
            steps.append(step)
        elif step.upper() == "S": # down
            if coordsOfKing[0] != 1: # should not step to negative!
                coordsOfKing[0] -= 1 #mistake
            printBoard(coordsOfKing)
            steps.append(step)
        elif step.upper() == "W": # up
            if coordsOfKing[0] != rows: # should not step from the table!
                coordsOfKing[0] += 1 #mistake
            printBoard(coordsOfKing)
            steps.append(step)
        elif step.upper() == "R":
            repeatSteps(steps)
        elif step.upper() == "X": # exit
            break
        else:
            print("False input") # ####### to write

 
coordsOfKing = [1, 5] # start coordinates of the King: 1,5 (1st row, 5th cell)
printBoard(coordsOfKing)
askTheUser(coordsOfKing)
printBoard(coordsOfKing)