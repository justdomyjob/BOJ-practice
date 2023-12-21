import sys
N= int(input())
power = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]

team = [0]

min_difference = 10**8

def dfs(n,idx):
    global min_difference
    if n == N//2:
        other_team = [i for i in range(N)]

        for t in team:
            other_team.remove(t)

        difference = 0

        for t1 in team:
            for t2 in team:
                if t1==t2:
                    continue
                difference += power[t1][t2]

        for t1 in other_team:
            for t2 in other_team:
                if t1==t2:
                    continue
                difference -= power[t1][t2]

        min_difference = min(min_difference,abs(difference))
        return
    for i in range(idx,N):
        if i not in team:
            team.append(i)
            dfs(n+1,i+1)
            team.pop()
dfs(1,0)
print(min_difference)