def solution(n, build_frame):
    N,G,B,A =0,1,2,3
    graph = [[N for _ in range(n+1)] for _ in range(n+1)]

    def check(): #모든 보,기에 대해서 성립
        for i in range(n+1):
            for j in range(n+1):
                if graph[i][j] & G == G: #기일때
                    if i==0:
                        continue
                    try:
                        if graph[i-1][j] & G ==G:
                            continue
                    except:
                        pass
                    if graph[i][j] & B == B:
                        continue
                    try:
                        if graph[i][j-1] & B == B:
                            continue
                    except:
                        pass
                    return False
        for i in range(n + 1):
            for j in range(n + 1):
                if graph[i][j] & B == B:
                    try:
                        if graph[i-1][j] & G ==G:
                            continue
                    except:
                        pass
                    try:
                        if graph[i-1][j+1] & G ==G:
                            continue
                    except:
                        pass
                    try:
                        if graph[i][j-1] & B == B and graph[i][j+1] & B == B:
                            continue
                    except:
                        pass
                    return False
        return True
    def del_gi(x,y):
        graph[y][x] -= G
        if check():
            pass
        else:
            graph[y][x] += G
    def add_gi(x,y):
        graph[y][x] += G
        if check():
            pass
        else:
            graph[y][x] -=G
    def del_bo(x,y):
        graph[y][x] -= B
        if check():
            pass
        else:
            graph[y][x] += B
    def add_bo(x,y):
        graph[y][x] += B
        if check():
            pass
        else:
            graph[y][x] -= B

    for x,y,a,b in build_frame:
        if a==0:
            if b==0:
                del_gi(x, y)
            elif b==1:
                add_gi(x,y)
        elif a ==1: #보
            if b == 0:
                del_bo(x,y)
            elif b == 1:
                add_bo(x,y)
    ret = []
    for i in range(n+1):
        for j in range(n+1):
            if graph[i][j] & G ==G:
                ret.append((j,i,0))
            if graph[i][j] & B ==B:
                ret.append((j,i,1))
    ret.sort()
    return ret
