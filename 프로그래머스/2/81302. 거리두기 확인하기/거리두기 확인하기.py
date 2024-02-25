from collections import deque

dy = [-1,0,1,0]
dx = [0,1,0,-1]
def solution(places):
    answer = []
    for place in places:
        a = detect(place)
        answer.append(a)
    
    return answer

def detect(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                a = bfs(place,i,j)
                if a==False:
                    return 0
    return 1
        
def bfs(place, i, j):
    visited = [[-1 for _ in range(5)] for _ in range(5)]
    visited[i][j] = 0
    q = deque()
    q.append((i,j))
    while q:
        i,j = q.popleft()
        for k in range(4):
            ni = i + dy[k]
            nj = j + dx[k] 
            if 0<=ni<5 and 0<=nj<5 and visited[ni][nj] == -1 and place[ni][nj]!= "X":
                visited[ni][nj] = visited[i][j] +1
                q.append((ni,nj))
                if place[ni][nj] == "P" and 1<=visited[ni][nj]<=2:
                    return False
    return True