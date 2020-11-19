# Programm name: My version of "King's walk"
# 15 Nov, 2020  Made by Selim ALtayev, vw9e6b
# Modifications: main functionality, row numbers(1-8), column letters(A-H), passed steps are shown with stars, replay function, random steps, reset are aviable

# Input: w, s, d, a or x to quit (extensions: "random" to make random step, "replay" to replay all steps made before)
# Output: chess table


import random
import time
rows = 9
line = "-" * 54
#creates an empty 2-dimensional list
mainBoard = [["     " for i in range(rows)] for j in range(rows)]
king = "  K  "
star = "  *  "
#default king position
defX, defY = 1, 1



#Assigns (A-H) column and (1-8) row
def setBoard(board):
    board[0][0] = "     "
    for i in range(1, rows):
		#for (1-8) row
        board[0][i] = "  " + str(i) + "  "
		#for (A-H) column
        board[i][0] = "  " + chr(65 + i - 1) + "  "

#prints main board
def printBoard(board):
    for i in range(rows):
        for j in range(rows):
            print(board[j][i], end="|")
        print("\n" + line)

# Here position changing functions are coming
def Up(x, y):
    if y == 1:
        return [x, y]
    return [x, y - 1]


def Down(x, y):
    if y == 8:
        return [x, y]
    return [x, y + 1]


def Left(x, y):
    if x == 1:
        return [x, y]
    return [x - 1, y]


def Right(x, y):
    if x == 8:
        return [x, y]
    return [x + 1, y]
# Here position changing function end

#Resets the board and moves King to the default positon
def resetAll():
    for i in range(1, rows):
        for j in range(1, rows):
            mainBoard[i][j] = "     "
    mainBoard[1][1] = king


#Uses list with all steps to repeat them
def repeatAll(steps):
    resetAll()
    x, y = 1, 1
    printBoard(mainBoard)
    for step in steps:
        oldX, oldY = x, y #Store the coordinates in new variables
        if step.upper() == "W": #If input matches 
            x, y = Up(x, y) # Change the coordinate of the King
            mainBoard[x][y] = king #Prints the King on a board 
            if oldX == x and oldY == y: 
                pass # does nothing
            else: mainBoard[oldX][oldY] = star #Prints star where the King was

        elif step.upper() == "S":
            x, y = Down(x, y)
            mainBoard[x][y] = king
            if oldX == x and oldY == y: 
                pass
            else: mainBoard[oldX][oldY] = star
        
        elif step.upper() == "A":
            x, y = Left(x, y)
            mainBoard[x][y] = king
            if oldX == x and oldY == y: 
                pass
            else: mainBoard[oldX][oldY] = star
        
        elif step.upper() == "D":
            x, y = Right(x, y)
            mainBoard[x][y] = king
            if oldX == x and oldY == y: 
                pass
            else: mainBoard[oldX][oldY] = star
        printBoard(mainBoard)
        print()
        time.sleep(2)
    print("REPEAT HAS DONE!\n")



# Main part
mainBoard[defX][defY] = king
setBoard(mainBoard)
printBoard(mainBoard)
allSteps = []
while True:
    oldX, oldY = defX, defY
    command = input("""Enter one of the commands:
    1) 'W', 'S', 'A' or 'D' to move to one of the directions
    2) 'random' to move to random direction
    3) 'repeat' to repeat all steps done
    4) 'reset' to clear the board
    5) 'X' to leave the program\n""")

    if command.lower() == "random": command = random.choice(["W", "S", "A", "D"])

    if command.upper() == "W":
        allSteps.append(command)
        defX, defY = Up(defX, defY)
        mainBoard[defX][defY] = king
        if oldX == defX and oldY == defY: 
            pass
        else: mainBoard[oldX][oldY] = star
    
    elif command.upper() == "S":
        allSteps.append(command)
        defX, defY = Down(defX, defY)
        mainBoard[defX][defY] = king
        if oldX == defX and oldY == defY: 
            pass
        else: mainBoard[oldX][oldY] = star
    
    elif command.upper() == "A":
        allSteps.append(command)
        defX, defY = Left(defX, defY)
        mainBoard[defX][defY] = king
        if oldX == defX and oldY == defY: 
            pass
        else: mainBoard[oldX][oldY] = star
    
    elif command.upper() == "D":
        allSteps.append(command)
        defX, defY = Right(defX, defY)
        mainBoard[defX][defY] = king
        if oldX == defX and oldY == defY: 
            pass
        else: mainBoard[oldX][oldY] = star

    elif command.lower() == "repeat":
        mainBoard[defX][defY] = "     "
        repeatAll(allSteps)
        allSteps.clear()

    elif command.upper() == "X": break
    elif command.lower() == "reset":
        defX, defY = 1, 1
        resetAll()
    else: print("INVALID INPUT!\n")

    printBoard(mainBoard)
