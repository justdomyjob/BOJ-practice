N = int(input())
blocks = [list(map(int,input().split())) for _ in range(N)]

graph = [[0 for _ in range(10)] for _ in range(10)]

def pp():
    for g in graph:
        print(g)
    print()

score = 0


def move_row_line(row):
    for j in range(row, 3, -1):
        graph[j][:4] = graph[j - 1][:4]

def make_row(row):
    for i in range(row, 4, -1):
        if graph[i][:4] == [0, 0, 0, 0]:
            move_row_line(i)
            make_row(row-1)

def move_col_line(col):
    for j in range(col, 3, -1):
        graph[0][j] = graph[0][j-1]
        graph[1][j] = graph[1][j-1]
        graph[2][j] = graph[2][j-1]
        graph[3][j] = graph[3][j-1]

def make_col(col):
    for j in range(col, 4, -1):
        if graph[0][j] == graph[1][j] == graph[2][j] == graph[3][j] == 0:
            move_col_line(j)
            make_col(col-1)

def remove_line():
    global score
    for i in range(6,10):
        if graph[i][:4] == [1,1,1,1]:
            score+=1
            graph[i][:4] = [0,0,0,0]
    for j in range(6,10):
        if graph[0][j] == graph[1][j] == graph[2][j] == graph[3][j] ==1:
            score+=1
            graph[0][j], graph[1][j], graph[2][j], graph[3][j] =0,0,0,0

    make_row(9)
    make_row(9)
    make_col(9)
    make_col(9)

def move_line():
    row5 = graph[4][:4]
    row6 = graph[5][:4]
    col5 = [graph[0][4], graph[1][4], graph[2][4], graph[3][4]]
    col6 = [graph[0][5], graph[1][5], graph[2][5], graph[3][5]]

    if 1 in row5 and 1 in row6:
        move_row_line(9)
        move_row_line(9)
    elif 1 in row5 or 1 in row6:
        move_row_line(9)
    if 1 in col5 and 1 in col6:
        move_col_line(9)
        move_col_line(9)
    elif 1 in col5 or 1 in col6:
        move_col_line(9)

for t,y,x in blocks:
    if t == 1:
        for i in range(4,10):
            if i ==9:
                graph[i][x] = 1
                break
            if graph[i+1][x] == 1:
                graph[i][x] = 1
                break
        for i in range(4,10):
            if i == 9:
                graph[y][i] =1
                break
            if graph[y][i+1] ==1:
                graph[y][i] = 1
                break
    elif t==2:
        for i in range(4,10):
            if i == 9:
                graph[i][x], graph[i][x + 1] = 1, 1
                break
            if graph[i+1][x] == 1 or graph[i+1][x+1] ==1:
                graph[i][x], graph[i][x+1] = 1,1
                break
        for i in range(4,9):
            if i == 8:
                graph[y][i], graph[y][i + 1] = 1, 1
                break
            if graph[y][i+2]==1 and graph[y][i+1] ==0  and graph[y][i] ==0:
                graph[y][i], graph[y][i+1] = 1,1
                break
    elif t==3:
        for i in range(4,9):
            if i == 8:
                graph[i][x], graph[i+1][x] =1,1
                break
            if graph[i+2][x] == 1 and graph[i+1][x] == 0 and graph[i][x] == 0:
                graph[i][x],graph[i+1][x] = 1,1
                break
        for i in range(4, 10):
            if i == 9:
                graph[y][i], graph[y + 1][i] = 1, 1
                break
            if graph[y][i+1] == 1 or graph[y+1][i+1] ==1:
                graph[y][i], graph[y+1][i] = 1,1
                break

    remove_line()
    move_line()
count = 0
print(score)
for i in range(6,10):
    for j in range(4):
        if graph[i][j] == 1:
            count+=1
for i in range(4):
    for j in range(6,10):
        if graph[i][j] ==1:
            count+=1
print(count)
