try : standard_input = open("input.txt", "r")  
except:pass

n, m =map(int,input().split())
chess = [input() for _ in range(n)]
chess1 = [[0 for _ in range(m)] for _ in range(n)]
chess2 = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if (i+j)%2==0 and chess[i][j] == "W":
            chess1[i][j]=1
        elif (i+j)%2==1 and chess[i][j] == "W":
            chess2[i][j]=1
        elif (i+j)%2==0 and chess[i][j] == "B":
            chess2[i][j]=1
        else:
            chess1[i][j]=1
sum = 64
for i in range(n-7):
    for j in range(m-7):
        sum1 = 0
        sum2 = 0
        for k in range(8):
            for l in range(8):
                sum1 += chess1[i+k][j+l]
                sum2 += chess2[i+k][j+l]
        if min(sum1,sum2) < sum:
            sum = min(sum1,sum2)
print(sum)