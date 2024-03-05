import copy

dy = [-1,0,1,0]
dx = [0,1,0,-1]
def solution(board, aloc, bloc):
    r = len(board)
    c = len(board[0])
    def A_win(board,aloc,bloc): #A가 이기면 True이면서 가장 작은 값 수 지면 False 이면서 가장 큰 값

        #초기값
        y,x = aloc
        if board[y][x] == 0:
            return False,0

        ret = [] #모든 값이 -1이면 -1 리턴 하나라도 있으면 그 수 +1
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < r and 0<= nx < c and board[ny][nx]==1:
                new_board = copy.deepcopy(board)
                new_board[y][x] = 0
                ret.append(A_win(new_board,bloc,[ny,nx]))  #둘의 위치를 바꿔줘야됨
        if not ret:
            return False,0
        else:
            ret = [(not i[0],i[1]) for i in ret]
            win = False
            for trueFalse, number in ret:
                win = win | trueFalse
            if win:
                maximum = 10**9
                for trueFalse, number in ret:
                    if trueFalse:
                        maximum = min(maximum,number)
                return True,maximum+1
            else:
                numbers = [i[1] for i in ret]
                count = max(numbers)
                return False,count+1
    print(A_win(board,aloc,bloc))
    return A_win(board,aloc,bloc)[1]
# solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]],[1,0],[1,2])
# solution([[1, 1, 1], [0, 0, 0], [1, 1, 1]],[0,1],[0,1])
# solution([[1, 1, 1, 1, 1]],[0,0],[0,4])
# solution(	[[1, 1, 1], [0, 0, 1], [1, 1, 1]], [1, 2], [0, 0])