def solution(board, moves):
    stack = []
    ret = 0
    for column in moves:
        column -=1
        for i in range(len(board)):
            if board[i][column] !=0:
                if stack and stack[-1] == board[i][column]:
                    stack.pop()
                    ret+=2
                else:
                    stack.append(board[i][column])
                board[i][column] = 0
                break
    return ret