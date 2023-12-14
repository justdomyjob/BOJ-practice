try : standard_input = open("input.txt", "r")  
except:pass
import sys
N, M =map(int,sys.stdin.readline().rstrip().split())
table = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]


row_sum_table = []
for i in range(N):
    one_row_table =[]
    for j in range(N):
        try:
            one_row_table.append(one_row_table[-1]+table[i][j])
        except:
            one_row_table.append(table[i][j])
    row_sum_table.append(one_row_table)

all_sum_table =[[0 for _ in range(N)] for _ in range(N)]
for j in range(N):
    for i in range(N):
        if i>=1:
            all_sum_table[i][j] = all_sum_table[i-1][j] + row_sum_table[i][j]
        else:
            all_sum_table[i][j] = row_sum_table[i][j]
for _ in range(M):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().rstrip().split())
    x1 = x1-1
    y1 = y1-1
    x2 = x2-1
    y2 = y2-1
    big = all_sum_table[x2][y2]
    small = all_sum_table[x1-1][y1-1]
    row = all_sum_table[x1-1][y2]
    col = all_sum_table[x2][y1-1]
    ans = big - row - col + small
    if x1>=1 and y1>=1 :
        ans = big - row - col + small
    elif x1>=1 and y1==0 :
        ans = big - row 
    elif x1==0 and y1>=1 :
        ans = big - col 
    else:
        ans =all_sum_table[x2][y2] 
    print(ans)

