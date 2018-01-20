import random
from copy import deepcopy

originalBoard=[]
baseScore = 100000

def initBoard(m,n):
    for i in range(n):
        temp=[]
        for j in range(m):
            temp.append(' ')
        originalBoard.append(temp)


def printBoard(board):
    print "\n"
    for i in range(n):
        for j in range(m):
            print "| "+board[i][j],
        print "|"
        print " "+"-"*(4*m-1)
    print "\n"

print "AI - X\nYou - O\n"

def assignStartingPlayer():
    temp = random.randint(0,10)
    return 'X' if temp%2==0 else 'O'


m=7 # columns
n=6 # rows
initBoard(m,n)
startPlayer = assignStartingPlayer()

# printBoard()


def isGameOver(board,depth,score):
    availableMoves = getAvailableStates(board)
    countValidMoves = 0
    for i in availableMoves:
        if i!=-1:
            countValidMoves+=1
    if depth == 0 or score==baseScore or score==-baseScore or countValidMoves==0:
        return True

    # print "returning false"
    return False


def getAvailableStates(board):
    temp=[-1]*m
    for i in range(n):
        for j in range(m):
            if board[i][j]==' ':
                temp[j]=i
    return temp

def individualScore(board,r,c,d_y,d_x):
    # printBoard(board)
    hp = 0
    cp = 0
    for i in range(4):
        if board[r][c] == "O":
            hp+=1
        elif board[r][c] == "X":
            cp+=1
        r += d_y
        c += d_x

    if hp == 4:
        return -baseScore
    elif cp == 4:
        return baseScore
    else:
        return cp


def getScore(board):

    totalPoints = 0
    for row in range(n-3):
        for column in range(m):
            score = individualScore(board,row, column, 1, 0)
            if score == baseScore:
                return baseScore
            if score == -baseScore:
                return -baseScore
            totalPoints += score


    for row in range(n):
        for column in range(m-3):
            score = individualScore(board,row, column, 0, 1)
            if score == baseScore:
                return baseScore
            if score == -baseScore:
                return -baseScore
            totalPoints += score

    for row in range(n-3):
        for column in range(m-3):
            score = individualScore(board,row, column, 1, 1)
            if score == baseScore:
                return baseScore
            if score == -baseScore:
                return -baseScore
            totalPoints += score

    for row in range(n):
        for column in range(m-3):
            score = individualScore(board,row, column, -1, 1)
            if score == baseScore:
                return baseScore
            if score == -baseScore:
                return -baseScore
            totalPoints += score

    return totalPoints



def maximize(depth,board):

    score = getScore(board)
    if isGameOver(board,depth,score):
        return [-1, score]

    maxi = [-1,-99999]

    availableMoves = getAvailableStates(board)
#     print availableMoves
    for i in range(len(availableMoves)):
#         print "aasdsds"
        if availableMoves[i]!=-1:
#             print "aasdsds"
            tempBoard = deepcopy(board)
        
            tempBoard[availableMoves[i]][i] = "X"

            bestMove = minimize(depth-1,tempBoard)

            if maxi[0]==-1 or bestMove[1] > maxi[1]:
                maxi[0] = i
                maxi[1] = bestMove[1]

            # tempBoard[availableMoves[i]][i] = " "         
    return maxi


def minimize(depth,board):


    if isGameOver(board, depth,score):
        return [-1, score]
    mini = [-1,99999]

    availableMoves = getAvailableStates(board)
    for i in range(len(availableMoves)):
#         print "aasdsds"
        if availableMoves[i]!=-1:

            tempBoard = deepcopy(board)
            
            tempBoard[availableMoves[i]][i] = "O"
            bestMove = maximize(depth-1,tempBoard)

            if mini[0]==-1 or bestMove[1] < mini[1]:
                mini[0] = i
                mini[1] = bestMove[1]

            # tempBoard[availableMoves[i]][i] = " "

    return mini
    

print 'Computer is starting first\n' if startPlayer=='X' else 'You are starting first\n'
# player = startPlayer
player = 'O'

depth = 4


score = getScore(originalBoard)

while not isGameOver(originalBoard,depth,score) or isGameOver(originalBoard,depth,score):
    if player=='O':
        availableMoves = getAvailableStates(originalBoard)
        humanMove = input('Your turn. Enter a column between 1 and '+str(m)+' : ')
        while int(humanMove)<1 or int(humanMove)>m:
            print "Enter a valid move",
            humanMove = input('Your turn. Enter a column between 1 and '+str(m)+' : ')
        while availableMoves[humanMove-1]==-1:
            print "Column "+str(humanMove)+" is already full"
            humanMove = input('Choose another column : ')
            while int(humanMove)<1 or int(humanMove)>m:
                print "Enter a valid move",
                humanMove = input('Your turn. Enter a column between 1 and '+str(m)+' : ')

        originalBoard[availableMoves[humanMove-1]][humanMove-1]='O'
        player='X'
    else:
        bestMove = maximize(depth,originalBoard)
        
        availableMoves = getAvailableStates(originalBoard)
        
        originalBoard[availableMoves[bestMove[0]]][bestMove[0]] = 'X'
        player = 'O'
        print "Computer made a move"
        printBoard(originalBoard)
        
        
    score = getScore(originalBoard)
    if isGameOver(originalBoard, depth, score):
        print "Game over"
        exit()

print "Game over"
