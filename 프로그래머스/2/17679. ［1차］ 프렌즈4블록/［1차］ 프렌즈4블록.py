def solution(m, n, board):
    board = [list(array) for array in board]
    while True:
        temp = [array[:] for array in board]
        have = False
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j]==board[i][j+1]==board[i+1][j]==board[i+1][j+1]!="x":
                    temp[i][j],temp[i][j+1],temp[i+1][j],temp[i+1][j+1] = "x","x","x","x"
                    have=True
        if not have:
            s = 0
            for i in range(m):
                for j in range(n):
                    if board[i][j] == "x":
                        s+=1
            return s


        for i in range(m-1,-1,-1):
            for j in range(n):
                countX = 0
                for k in range(i+1,m):
                    if temp[k][j] =="x":
                        countX+=1
                if countX==0:
                    continue
                if temp[i][j]=="x":
                    board[i][j] = "x"
                board[i+countX][j] = board[i][j]
                board[i][j] = "x" 


