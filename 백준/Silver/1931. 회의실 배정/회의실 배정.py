try : standard_input = open("input.txt", "r")  
except:pass

n = int(input())
meetings =[list(map(int,input().split())) for _ in range(n)]

meetings.sort(key = lambda x: [x[1],x[0]])

finish_time = 0
ans = 0
for meeting in meetings:
    if meeting[0] >= finish_time:
        ans+=1
        finish_time = meeting[1]
print(ans)