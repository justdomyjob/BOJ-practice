try : standard_input = open("input.txt", "r")  
except:pass

n = int(input())
map = [input().rstrip() for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
steps = [[0,1],[1,0],[-1,0],[0,-1]]
def E(x,y):
    ulist = []
    for step in steps:
        move = [a+b for a,b in zip(step,[x,y])]
        x1,y1 = move
        if 0<= x1 <= n-1 and 0<= y1 <= n-1 and map[x1][y1]=="1":
            ulist.append(move)
    return ulist

def dfs(x,y):
    home = 1
    visited[x][y] = 1
    for u in E(x,y):
        x1,y1 = u
        if visited[x1][y1] ==0:
            visited[x1][y1] = 1
            home += dfs(x1,y1)
    return home
home_list = []
for i in range(n):
    for j in range(n):
        if map[i][j]=="1" and visited[i][j]==0:
            home_list.append(dfs(i,j))
home_list.sort()
print(len(home_list))
for home in home_list:
    print(home)
