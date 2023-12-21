try : standard_input = open("input.txt", "r")  
except:pass

n, m =map(int,input().split())

s = []
def dfs():
    if len(s)==m:
        print(" ".join(map(str,s)))
    else:
        for i in range(1,n+1):
            s.append(i)
            dfs()
            s.pop()
dfs()