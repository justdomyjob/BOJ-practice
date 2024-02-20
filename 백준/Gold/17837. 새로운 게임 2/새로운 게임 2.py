N,K = map(int,input().split())
color_graph = [list(map(int, input().split())) for _ in range(N)]
WHITE,RED,BLUE = 0,1,2
horses = [list(map(int,input().split())) for _ in range(K)]
RIGHT,LEFT,UP,DOWN = 1,2,3,4
dic={}
dic[RIGHT] = (0,1)
dic[LEFT] = (0,-1)
dic[UP] = (-1,0)
dic[DOWN] = (1,0)

horse_graph = [[[] for _ in range(N)] for _ in range(N)]

#초기
horses = [[r-1,c-1,d] for r,c,d in horses]

for horse,(r,c,d) in enumerate(horses):
    r,c= r,c
    horse_graph[r][c].append(horse)

def check():
    for i in range(N):
        for j in range(N):
            if len(horse_graph[i][j]) >= 4:
                return True
    return False
def pp():
    for g in horse_graph:
        print(g)
    print()
def move():
    for horse,(r,c,d) in enumerate(horses):
        r,c= r,c
        nr = r + dic[d][0]
        nc = c + dic[d][1]
        if 0 <= nr < N and 0 <= nc < N:
            color = color_graph[nr][nc]
        else:
            color = BLUE
        if color ==WHITE:
            my_horses = horse_graph[r][c]
            cut_index = my_horses.index(horse)
            horse_graph[nr][nc].extend(my_horses[cut_index:])
            horse_graph[r][c] = my_horses[:cut_index]
            for index in my_horses[cut_index:]: #위에 탄 말들 위치 바꿔줌
                horses[index][0] = nr
                horses[index][1] = nc
        elif color ==RED:
            my_horses = horse_graph[r][c]
            cut_index = my_horses.index(horse)
            horse_graph[nr][nc].extend(my_horses[cut_index:][::-1])
            horse_graph[r][c] = my_horses[:cut_index]
            for index in my_horses[cut_index:]:  # 위에 탄 말들 위치 바꿔줌
                horses[index][0] = nr
                horses[index][1] = nc
        elif color==BLUE:
            if d==UP:
                d = DOWN
            elif d==DOWN:
                d = UP
            elif d==RIGHT:
                d = LEFT
            elif d==LEFT:
                d = RIGHT
            horses[horse][2] = d
            nr = r + dic[d][0]
            nc = c + dic[d][1]
            if 0<=nr<N and 0<=nc<N:
                color = color_graph[nr][nc]
            else:
                color = BLUE
            if color==BLUE:
                continue
            else:
                if color == WHITE:
                    my_horses = horse_graph[r][c]
                    cut_index = my_horses.index(horse)
                    horse_graph[nr][nc].extend(my_horses[cut_index:])
                    horse_graph[r][c] = my_horses[:cut_index]
                    for index in my_horses[cut_index:]:  # 위에 탄 말들 위치 바꿔줌
                        horses[index][0] = nr
                        horses[index][1] = nc
                elif color == RED:
                    my_horses = horse_graph[r][c]
                    cut_index = my_horses.index(horse)
                    horse_graph[nr][nc].extend(my_horses[cut_index:][::-1])
                    horse_graph[r][c] = my_horses[:cut_index]
                    for index in my_horses[cut_index:]:  # 위에 탄 말들 위치 바꿔줌
                        horses[index][0] = nr
                        horses[index][1] = nc
        if check():
            return True
        else:
            continue
    return False

for i in range(1,1001):
    if move():
        print(i)
        exit(0)

print(-1)