dy = [-1,0,1,0]
dx = [0,1,0,-1]
from collections import deque
def solution(game_board, table):
    block_list = []
    N = len(game_board)
    visited = [[0 for _ in range(N)] for _ in range(N)]
    def bfs_table(y,x,visited):   
        visited[y][x] = 1
        block = [(y,x)]
        q = deque()
        q.append((y,x))
        while q:
            y, x = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0<=ny<N and 0<=nx<N and visited[ny][nx] == 0 and table[ny][nx] !=0:
                    visited[ny][nx] = 1
                    q.append((ny,nx))
                    block.append((ny,nx))
        block.sort()
        block1 = sorted(move(block))
        block2 = move(sorted(rotate(block1)))
        block3 = move(sorted(rotate(block2)))
        block4 = move(sorted(rotate(block3)))
        block_list = [block1,block2,block3,block4]
    
        return block_list
    
    def bfs_game(y,x,visited2):   
        visited2[y][x] = 1
        block = [(y,x)]
        q = deque()
        q.append((y,x))
        while q:
            y, x = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0<=ny<N and 0<=nx<N and visited2[ny][nx] == 0 and game_board[ny][nx] ==0:
                    visited2[ny][nx] = 1
                    q.append((ny,nx))
                    block.append((ny,nx))
        block.sort()
        block = move(block)
        return block
    
    def move(block):
        y1,x1 = block[0]
        block = [(y-y1,x-x1) for y,x in block]
        return block
    def rotate(block):
        new_block = [(-x,y) for y,x in block]
        return new_block
    
    visited2 = [[0 for _ in range(N)] for _ in range(N)] 
    
    all_block = []
    for y in range(N):
        for x in range(N):
            if table[y][x]==1 and visited[y][x]==0 :
                all_block.append(bfs_table(y,x,visited))
        
    compare_block = []
    for y in range(N):
        for x in range(N):
            if game_board[y][x] == 0 and visited2[y][x] == 0:
                a = bfs_game(y,x,visited2)
                compare_block.append(a)
    # for block_list in all_block:
    #     print(block_list)  
    # print()
    # for block in compare_block:
    #     print(block)
        
    ret = 0
    for block in compare_block:
        for block_list in all_block:
            if block in block_list:
                all_block.remove(block_list)
                ret += len(block)
                # print(block)
                break
    return ret