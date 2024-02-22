N = int(input())

graph = [[0 for _ in range(N)] for _ in range(N)]

dy = [-1,0,1,0]
dx = [0,1,0,-1]
place = {}
like_set = {}
for _ in range(N**2):
    a,b,c,d,e = map(int,input().split())
    like_set[a] = set({b,c,d,e})
    cond1 = [[0 for _ in range(N)] for _ in range(N)]
    for friend in like_set[a]:
        if friend in place:
            y,x = place[friend]
            for k in range(4):
                ny =  y + dy[k]
                nx =  x + dx[k]
                if 0<=ny<N and 0<=nx<N and graph[ny][nx] == 0:
                    cond1[ny][nx] +=1
    maximum = 0
    for i in range(N):
        for j in range(N):
            maximum = max(maximum,cond1[i][j])
    cond1_list =[]
    for i in range(N):
        for j in range(N):
            if cond1[i][j] == maximum  and graph[i][j] == 0 :
                cond1_list.append((i,j))

    if len(cond1_list) ==1:
        y,x = cond1_list[0]
        graph[y][x] = a
        place[a] = (y,x)
        continue

    else:
        cond2_list = []
        for y,x in cond1_list:
            count = 0
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]
                if 0<=ny<N and 0<=nx<N and graph[ny][nx] == 0:
                    count+=1
            cond2_list.append((-count,y,x))
        cond2_list.sort()
        count,y,x = cond2_list[0]
        graph[y][x] = a
        place[a] = (y,x)


score = 0
for j in range(N):
    for i in range(N):
        likes = 0
        for k in range(4):
            ni = i + dy[k]
            nj = j + dx[k]
            if 0<=ni<N and 0<=nj<N and graph[ni][nj] in like_set[graph[i][j]]:
                likes+=1
        if likes ==1:
            score+=1
        elif likes==2:
            score+=10
        elif likes==3:
            score+=100
        elif likes==4:
            score+=1000
print(score)

