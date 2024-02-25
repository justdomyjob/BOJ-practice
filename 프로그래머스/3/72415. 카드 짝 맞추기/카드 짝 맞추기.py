from collections import defaultdict, deque

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def solution(board, r, c):
    answer = bfs(board,r,c)
    return answer

def bfs(board,i,j):
    minimum = 10**7
    visited = set()
    back_card_set = set()
    for r in range(4):
        for c in range(4):
            if board[r][c] >0:
                back_card_set.add((r,c))
    visited.add((frozenset(back_card_set),(-1,-1),(i,j)))
    q = deque()
    q.append((frozenset(back_card_set),(-1,-1),(i,j),0))
    while q:
        back_card_set, (r,c), (i,j),count = q.popleft()
        if len(back_card_set) == 0:
            minimum = min(minimum,count)
        for k in range(4):
            ni = i + dy[k]
            nj = j + dx[k]
            if 0<=ni < 4 and 0<= nj <4 and (back_card_set, (r,c), (ni,nj)) not in visited:
                visited.add((back_card_set, (r,c), (ni,nj)))
                q.append((back_card_set, (r,c), (ni,nj),count+1))

            for s in range(1,4):
                si = i + dy[k] * s
                sj = j + dx[k] * s
                if 0<=si <4 and 0<=sj <4 and (si,sj) in back_card_set :
                    break
                elif 0<=si <4 and 0<=sj <4 and (si,sj) not in back_card_set :
                    continue
                else:
                    si = si - dy[k]
                    sj = sj - dx[k]
                    break
            if (back_card_set, (r,c), (si,sj)) not in visited:
                visited.add((back_card_set, (r, c), (si, sj)))
                q.append((back_card_set, (r, c), (si, sj), count + 1))
        if r==-1 and c==-1:
            if board[i][j] != 0:
                if (i, j) in back_card_set:
                    if (back_card_set, (i, j), (i, j)) not in visited:
                        visited.add((back_card_set, (i, j), (i, j)))
                        q.append((back_card_set, (i, j), (i, j), count + 1))
        else:
            if board[i][j] != 0:
                if board[r][c] == board[i][j] and not(r==i and c==j):
                    temp_set = set(back_card_set)
                    temp_set.remove((r, c))
                    temp_set.remove((i, j))
                    temp_set = frozenset(temp_set)
                    if (temp_set, (-1, -1), (i, j)) not in visited:
                        visited.add((temp_set, (-1, -1), (i, j)))
                        q.append((temp_set, (-1, -1), (i, j), count + 1))
    return minimum
