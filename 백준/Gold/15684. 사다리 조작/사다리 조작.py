N,M,H = map(int,input().split())

graph = [[False for _ in range(N+1)] for _ in range(H+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a][b] = True


def check_sero(sero):
    temp = sero
    for h in range(1,H+1):
        if graph[h][sero] == True:
            sero+=1
        elif sero>=2 and graph[h][sero-1] == True:
            sero-=1
    if temp==sero:
        return True
    else:
        return False
# def check():
#     for sero in range(1,N+1):
#         if not check_sero(sero):
#             return False
#     return True

def check():
    for i in range(1,N+1):
        k = i
        for j in range(1,H+1):
            if graph[j][k]:
                k += 1
            elif k > 1 and graph[j][k-1]:
                k -= 1
        if i != k:
            return False
    return True

minimum = 4
def dfs(y,x,n):
    global minimum
    if check():
        minimum = min(n,minimum)
        return
    elif n == 3 or minimum <= n:
        return
    else:
        for i in range(y,H+1):
            if i==y:
                k= x
            else:
                k =1
            for j in range(k,N):
                if not graph[i][j] and not graph[i][j+1] and(j ==0 or not graph[i][j-1]):
                    graph[i][j] = True
                    dfs(i,j+2,n+1)
                    graph[i][j] = False
dfs(1,1,0)
if minimum==4:
    print(-1)
else:
    print(minimum)