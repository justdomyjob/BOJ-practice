ALL = -1
def solution(board):
    N = len(board)
    def add(board):
        for j in range(N):
            for i in range(N):
                if board[i][j] in [0, ALL]:
                    board[i][j] = ALL
                else:
                    break
    def check_and_remove(board):
        for i in range(N-2):
            for j in range(N-1):
                blocks = [board[i][j], board[i+1][j], board[i+2][j], board[i][j+1], board[i+1][j+1], board[i+2][j+1]]
                blocks.sort()
                if blocks[2]==blocks[3] ==blocks[4]==blocks[5] >=1 and blocks[0] == blocks[1] == ALL:
                    board[i][j], board[i+1][j], board[i+2][j], board[i][j+1], board[i+1][j+1], board[i+2][j+1] =0,0,0,0,0,0
                    # print("here1")
                    return True
        for i in range(N-1):
            for j in range(N-2):
                blocks = [board[i][j], board[i+1][j], board[i][j+1], board[i+1][j+1], board[i][j+2], board[i+1][j+2]]
                blocks.sort()
                if blocks[2]==blocks[3] ==blocks[4]==blocks[5] >=1 and blocks[0] == blocks[1] == ALL:
                    # print(blocks)
                    # print(i,j)
                    board[i][j], board[i+1][j], board[i][j+1], board[i+1][j+1], board[i][j+2], board[i+1][j+2] =0,0,0,0,0,0
                    # print("here2")
                    return True
        return False
    count = 0
    while True:
        add(board)
        if check_and_remove(board):
            count+=1
            continue
        else:
            break
    print(count)
    add(board)
#     for b in board:
#         print(b)
#     print()

#     print(check_and_remove(board))
#     for b in board:
#         print(b)
#     print()
#     add(board)
#     print(check_and_remove(board))
#     for b in board:
#         print(b)
#     print()
#     add(board)
#     for b in board:
#         print(b)
#     print()
    
#     print(check_and_remove(board))
#     for b in board:
#         print(b)
#     print()
    return count