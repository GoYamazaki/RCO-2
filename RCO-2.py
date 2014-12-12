def printBoard(board):
    for c in board:
        print(c)

def writeCToXAndY(board,x,y,c):
    board[y][x]=c

def writeATMToBoard(board,c):
    ii = len(board)
    for i in range(ii):
        while "@" in board[i]:
            board[i][board[i].index("@")] = c

def searchCharInBoard(board,c):
    ii = len(board)
    for i in range(ii):
        if c in board[i]:
            return board[i].index(c),i

    return -1,-1

def searchCharNextToTheChar(board,x,y):
    charL = []
    X = len(board[1])-1
    Y = len(board)-1

    if x!=0:
        charL.append(board[y][x-1])
    if x!=X:
        charL.append(board[y][x+1])
    if y!=0:
        charL.append(board[y-1][x])
    if y!=Y:
        charL.append(board[y+1][x])

    return (set(charL))




if __name__=="__main__":
    inBoard = ["023337777a","02223788aa","002436688a","104446998a","1114669bbb","15555599bb"]

    inChar = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    outChar = list("+-*/")
    totset = set()
    for i in range(len(inBoard)):
        l = list(inBoard[i])
        totset = totset | set(l)
        inBoard[i] = l

    totalLen = len(totset)

    for char in totset:
        #print("")
        clist = set()

        while searchCharInBoard(inBoard,char) != (-1,-1):
            x,y = searchCharInBoard(inBoard,char)
            clist = clist | searchCharNextToTheChar(inBoard,x,y)

            writeCToXAndY(inBoard,x,y,"@")

        clist = clist - set(inChar)-set(["@"])
        #print(clist)

        if(len(clist)>=4):
            print("Cannot solve")
            exit(0)

        for oc in outChar:
            if oc not in clist:
                writeATMToBoard(inBoard,oc)

    printBoard(inBoard)


