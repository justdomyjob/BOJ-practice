import copy

n = int(input())
#0:-> 1:위 2:<- 3:아래
RIGHT,UP,LEFT,DOWN = 0,1,2,3
graph = [[0 for _ in range(101)] for _ in range(101)]


dy,dx = [0,-1,0,1],[1,0,-1,0]

def next_generation(start_point, end_point, points):
    sy,sx = start_point
    y, x = end_point
    next_endpoint = (y-x+sx,x+y-sy)
    temp = []
    for y1,x1 in points:
        if y1==y and x1==x:
            continue
        next_y1, next_x1 = y-x+x1,x+y-y1
        temp.append((next_y1,next_x1))
    return next_endpoint,points + temp

def color(start_point, direction, generation):
    sy, sx = start_point
    end_y1 = sy + dy[direction]
    end_x1 = sx + dx[direction]
    end_point = (end_y1,end_x1)
    points = [start_point,end_point]

    if generation > 0:
        for _ in range(generation):
            end_point,points = next_generation(start_point,end_point,points)
    for y,x in points:
        graph[y][x] = 1

def count_rectangle():
    count = 0
    for i in range(100):
        for j in range(100):
            if graph[i][j]==graph[i][j+1]==graph[i+1][j]==graph[i+1][j+1]==1:
               count+=1
    return count

for _ in range(n):
    sx,sy,direction,generation =  map(int,input().split())
    color((sy,sx),direction,generation)
print(count_rectangle())
