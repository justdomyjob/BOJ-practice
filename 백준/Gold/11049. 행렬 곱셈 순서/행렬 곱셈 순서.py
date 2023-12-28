import sys


try : standard_input = open("input.txt", "r")  
except:pass

n = int(input())
MAX = 2**31
matrix = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    matrix.append((a,b))
dp = [[0 for _ in range(n)] for _ in range(n)]

def operations(matrix, dp, dif, start, seperate):
    op = ( dp[start][start+seperate] + dp[start+seperate+1][start+dif] 
                + matrix[start][0] * matrix[start+seperate][1] * matrix[start+dif][1] )
    return op

for dif in range(1, n+1):
    for start in range(0, n-dif):
        min_operation = MAX
        for seperate in range(dif):
            temp = operations(matrix, dp, dif, start, seperate)
            if temp < min_operation:
                min_operation = temp
        dp[start][start+dif] = min_operation
print(dp[0][n-1])

