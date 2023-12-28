try : standard_input = open("input.txt", "r")  
except:pass

n, m = map(int, input().split())
map_ = [list(map(int,input().split())) for _ in range(n)]
dp = [[-1 for _ in range(m)] for _ in range(n)]
dp[0][0]=1
def go(a,b):
    if dp[a][b]!=-1:
        return dp[a][b]
    path = 0
    if a > 0 and map_[a-1][b] > map_[a][b] : 
        path += go(a-1,b)
    if a < n-1 and map_[a+1][b] > map_[a][b] : 
        path += go(a+1,b)
    if b > 0 and map_[a][b-1] > map_[a][b] : 
        path += go(a,b-1)
    if b < m-1 and map_[a][b+1] > map_[a][b] : 
        path += go(a,b+1)
    dp[a][b] = path
    return path
print(go(n-1,m-1))