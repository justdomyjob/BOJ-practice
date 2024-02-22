n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

dy = [0,1,0,-1]
dx = [-1,0,1,0]

sand = 0
def pp():
    for g in graph:
        print(g)
    print()

def wind(y,x,d): #y,x에서 d방향으로 붐
    global sand
    ny = y+dy[d]
    nx = x+dx[d]

    alphay =  y+dy[d] *2
    alphax = x + dx[d] * 2

    p5y = y+dy[d] *3
    p5x = x + dx[d] * 3
    p5 = int(graph[ny][nx] * 0.05)

    p11y = y+dy[(d + 1) % 4]
    p11x = x + dx[(d + 1) % 4]
    p12y = y + dy[(d - 1) % 4]
    p12x = x + dx[(d - 1) % 4]
    p1 = int(graph[ny][nx] * 0.01)

    p71y = ny + dy[(d + 1) % 4]
    p71x = nx + dx[(d + 1) % 4]
    p72y = ny + dy[(d - 1) % 4]
    p72x = nx + dx[(d - 1) % 4]
    p7 = int(graph[ny][nx] * 0.07)

    p101y = alphay + dy[(d + 1) % 4]
    p101x = alphax + dx[(d + 1) % 4]
    p102y = alphay + dy[(d - 1) % 4]
    p102x = alphax + dx[(d - 1) % 4]
    p10 = int(graph[ny][nx] * 0.1)

    p21y = ny + dy[(d + 1) % 4] *2
    p21x = nx + dx[(d + 1) % 4] * 2
    p22y = ny + dy[(d - 1) % 4] * 2
    p22x = nx + dx[(d - 1) % 4] * 2
    p2 = int(graph[ny][nx] * 0.02)

    alpha = graph[ny][nx] - p5-2*p1-2*p7-2*p10-2*p2

    array = [(alphay,alphax,alpha),(p5y,p5x,p5), (p11y,p11x,p1), (p12y,p12x,p1), (p71y,p71x,p7), (p72y,p72x,p7),
             (p101y,p101x,p10),(p102y,p102x,p10), (p21y,p21x,p2), (p22y,p22x,p2)]

    for y,x,p in array:
        if 0<=y<n and 0<=x<n :
            graph[y][x] += p
        else:
            sand+=p
    graph[ny][nx] = 0
    return ny,nx

y = n//2
x = n//2
d= 0
repeat = 2
i = 0
while not (y==0 and x==0):
    y,x= wind(y,x,d)
    i += 1
    if i == repeat // 2:
        d = (d + 1) % 4
    if i == repeat:
        repeat += 2
        i = 0
        d = (d + 1) % 4
print(sand)
# for _ in range(49):
#     print(d)
#     i+=1
#     if i==repeat//2:
#         d = (d+1)%4
#     if i == repeat:
#         repeat+=2
#         i = 0
#         d = (d + 1) % 4
