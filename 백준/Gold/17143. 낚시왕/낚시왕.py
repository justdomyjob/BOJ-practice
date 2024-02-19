import copy

R,C,M = map(int,input().split())
graph = [[0 for _ in range(C)] for _ in range(R)]

up =1
down =2
right = 3
left =4
dic = {}
dic[up] = (-1,0)
dic[down] = (1,0)
dic[right] = (0,1)
dic[left] = (0,-1)

shark_info= {}
for _ in range(M):
    r,c,s,d,z = map(int,input().split()) #속력, 이동방향, 크기
    graph[r-1][c-1] = z
    shark_info[z] = [s,d]

def move():
    global graph
    moved_sharks = set()
    moved_sharks.add(0)
    temp_graph = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            size = graph[i][j]
            if size not in moved_sharks:
                moved_sharks.add(size)
                s,d = shark_info[size]
                ni = (i + dic[d][0] * s) % (2*(R-1))
                nj = (j + dic[d][1] * s) % (2*(C-1))
                reverse = False
                if ni > (R-1) :
                    ni =  2*(R-1) - ni
                    reverse = True
                if nj > (C-1):
                    nj =  2*(C-1) - nj
                    reverse = True
                # temp_s = s
                # while temp_s > 0:
                #     if not (0 <= ni + dic[d][0] * minus < R and 0 <= nj + dic[d][1] * minus < C):
                #         minus *= -1
                #     ni += dic[d][0] * minus
                #     nj += dic[d][1] * minus
                #     temp_s -= 1
                if temp_graph[ni][nj] < size:
                    temp_graph[ni][nj] = size
                    if not reverse:
                        continue
                    else:
                        if d == up or d == down:
                            shark_info[size][1] = up + down - d
                        elif d == right or d == left:
                            shark_info[size][1] = right + left - d
                else:
                    continue


    graph = temp_graph
def pp():
    for g in graph:
        print(g)
    print()

ret = 0
for j in range(C):
    for i in range(R):
        size = graph[i][j]
        if size > 0:
            graph[i][j] = 0
            ret+=size
            break
    move()

print(ret)
