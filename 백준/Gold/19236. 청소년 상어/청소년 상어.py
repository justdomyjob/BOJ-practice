import copy

SHARK = 0
DEAD = -1
graph =[]
answer = 0
for i in range(4):
    a1,b1,a2,b2,a3,b3,a4,b4 = map(int,input().split())
    line = [[a1,b1-1],[a2,b2-1],[a3,b3-1],[a4,b4-1]]
    graph.append(line)

steps = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
seq=0
def dfs(y,x,graph,count):
    global answer

    fish, dir = graph[y][x]
    count+=fish
    graph[y][x] = (SHARK, dir)
    for fish in range(1,17):
        move_fish(fish,graph)

    finish = True
    for i in range(1,4):
        ny = y + steps[dir][0] *i
        nx = x + steps[dir][1] *i
        if 0<=ny<4 and 0<=nx<4 and graph[ny][nx][0] != DEAD:
            temp_graph = copy.deepcopy(graph)
            temp_graph[y][x] = (DEAD, dir)
            dfs(ny,nx,temp_graph,count)
            finish = False
        elif 0<=ny<4 and 0<=nx<4 and graph[ny][nx][0] == DEAD:
            continue
        else:
            break
    if finish:
        answer = max(answer,count)
def move_fish(fish,graph):
    for y in range(4):
        for x in range(4):
            if graph[y][x][0] == fish:
                dir = graph[y][x][1]
                for k in range(8):
                    ny = y + steps[(dir + k) % 8][0]
                    nx = x + steps[(dir + k) % 8][1]
                    if 0 <= ny < 4 and 0 <= nx < 4 and graph[ny][nx][0] != SHARK:
                        graph[y][x][1] = (dir + k) % 8
                        graph[ny][nx], graph[y][x] = graph[y][x], graph[ny][nx]
                        break
                return
def pp(graph):
    global seq
    for g in graph:
        print(g)
    seq+=1
    print(seq)
answer = 0
dfs(0,0,graph, 0)
print(answer)