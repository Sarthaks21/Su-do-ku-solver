count = 0
def isFull(sudoku):
    for x in range(0, 9):
        for y in range(0, 9):
            if sudoku[x][y] == 0:
                #print('Not full yet!')
                return 0
    print('NOW FULL!')
    return 1
def printBoard(sudoku):
    #global sudoku
    print("\t\t\t\t")
    for x in range(0, 9):
        if x == 3 or x == 6:
            print("\t\t\t\t")
        for y in range(0, 9):
            if y == 3 or y == 6:
                print("", end=" ")
            print(sudoku[x][y], end=" ")
        print()
    print("\t\t\t\t")

'''def possibleSolutions(sudoku):
    #bolow code is for when poss is a dictionary
    poss = {}
    for i in range(0, 9):
        for j in range(0, 9):
            li= [i for i in range(1, 10)]
            if sudoku[i][j] == 0:
                #choosing starting and ending index for terminator
                poss = terminator(sudoku, li, i, j, poss, ((i//3)*3), ((i//3)*3+3), ((j//3)*3), ((j//3)*3+3))

    sudoku = boardSolver(sudoku, poss)

#    return sudoku'''

def merge(x,y):
    return x*10+y

def terminator(sudoku, i, j, rS, rE, cS, cE):
    #print('Running terminator() for the square: {}X{}. '.format(i,j))
#    print('3x3 box = {}x{} to {}x{} , i.e. {} to {} '.format(rS, cS, rE, cE, sudoku[rS][cS], sudoku[rE][cE]))
    #for checking in the 3X3 block
    li = [i for i in range(1, 10)]
    #print(li)
    if len(li) != 9:
        print('FOUND ERROR PART!!')
        exit(10)
    #print('rS = {}, rE = {}\ncS = {}, cE = {}'.format(rS, rE, cS, cE))
    for m in range(rS, rE):
        for n in range(cS, cE):
            if sudoku[m][n] != 0:
                a = sudoku[m][n]
     #           print('Removed: ',a)
      #          print('After removing: ',li)
                li.remove(a)
    #for checking in the row
    for m in range(0, 9):
        if sudoku[i][m]!=0:
            a = sudoku[i][m]
            if li.__contains__(a):
                li.remove(a)
    #for checking in the column
    for m in range(0, 9):
        if sudoku[m][j]!=0:
            a = sudoku[m][j]
            if li.__contains__(a):
                li.remove(a)
   # print(li)
    return li

def boardSolver(sudoku):
    global count
    count = count + 1

    #global sudoku
    #checking if the board is full or not
    if isFull(sudoku):
        print('Board solved successfully!'
              '-----------------------------------------')
        printBoard(sudoku)
        exit('yay')
    #finding 1st vacant spot
    a = 0
    b = 0
    for i in range(0, 9):
        for j in range(0, 9):
            if sudoku[i][j] == 0:
                #print('i = {}, j = {} '.format(i, j))
                a = i
                b = j
                break
        else:
            continue
        break
    sols = terminator(sudoku, a, b, (a//3)*3, (((a//3))*3)+3,(b//3)*3, (((b//3))*3)+3)

    for x in range (0, len(sols)):
        #print('Value inputed at {}X{}: {}'.format(a, b, sols[x]))
        sudoku[a][b] = sols[x]
        #printBoard(sudoku)

        boardSolver(sudoku)

    sudoku[a][b] = 0
    return


SudokuBoard = [[0 for x in range(9)] for x in range(9)]
SudokuBoard[0][0] = 0
SudokuBoard[0][1] = 3
SudokuBoard[0][2] = 0
SudokuBoard[0][3] = 8
SudokuBoard[0][4] = 0
SudokuBoard[0][5] = 0
SudokuBoard[0][6] = 1
SudokuBoard[0][7] = 0
SudokuBoard[0][8] = 0
SudokuBoard[1][0] = 5
SudokuBoard[1][1] = 0
SudokuBoard[1][2] = 0
SudokuBoard[1][3] = 0
SudokuBoard[1][4] = 6
SudokuBoard[1][5] = 0
SudokuBoard[1][6] = 0
SudokuBoard[1][7] = 4
SudokuBoard[1][8] = 0
SudokuBoard[2][0] = 0
SudokuBoard[2][1] = 0
SudokuBoard[2][2] = 0
SudokuBoard[2][3] = 0
SudokuBoard[2][4] = 0
SudokuBoard[2][5] = 0
SudokuBoard[2][6] = 0
SudokuBoard[2][7] = 0
SudokuBoard[2][8] = 0
SudokuBoard[3][0] = 0
SudokuBoard[3][1] = 0
SudokuBoard[3][2] = 0
SudokuBoard[3][3] = 0
SudokuBoard[3][4] = 1
SudokuBoard[3][5] = 0
SudokuBoard[3][6] = 0
SudokuBoard[3][7] = 0
SudokuBoard[3][8] = 0
SudokuBoard[4][0] = 0
SudokuBoard[4][1] = 7
SudokuBoard[4][2] = 0
SudokuBoard[4][3] = 0
SudokuBoard[4][4] = 0
SudokuBoard[4][5] = 3
SudokuBoard[4][6] = 0
SudokuBoard[4][7] = 2
SudokuBoard[4][8] = 0
SudokuBoard[5][0] = 9
SudokuBoard[5][1] = 0
SudokuBoard[5][2] = 0
SudokuBoard[5][3] = 4
SudokuBoard[5][4] = 0
SudokuBoard[5][5] = 0
SudokuBoard[5][6] = 0
SudokuBoard[5][7] = 0
SudokuBoard[5][8] = 6
SudokuBoard[6][0] = 0
SudokuBoard[6][1] = 1
SudokuBoard[6][2] = 0
SudokuBoard[6][3] = 0
SudokuBoard[6][4] = 0
SudokuBoard[6][5] = 7
SudokuBoard[6][6] = 0
SudokuBoard[6][7] = 0
SudokuBoard[6][8] = 5
SudokuBoard[7][0] = 0
SudokuBoard[7][1] = 0
SudokuBoard[7][2] = 6
SudokuBoard[7][3] = 0
SudokuBoard[7][4] = 2
SudokuBoard[7][5] = 0
SudokuBoard[7][6] = 0
SudokuBoard[7][7] = 8
SudokuBoard[7][8] = 0
SudokuBoard[8][0] = 4
SudokuBoard[8][1] = 0
SudokuBoard[8][2] = 0
SudokuBoard[8][3] = 9
SudokuBoard[8][4] = 0
SudokuBoard[8][5] = 0
SudokuBoard[8][6] = 3
SudokuBoard[8][7] = 0
SudokuBoard[8][8] = 0
printBoard(SudokuBoard)

#SudokuBoard = possibleSolutions(SudokuBoard)

boardSolver(SudokuBoard)