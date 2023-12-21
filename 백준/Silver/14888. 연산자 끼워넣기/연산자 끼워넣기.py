import sys

N = int(input())
numbers =  list(map(int,sys.stdin.readline().rstrip().split()))
operaters = list(map(int,sys.stdin.readline().rstrip().split())) #+ - x //

MAX_NUMBER = 10**9
MIN_NUMBER = -10**9
max_temp = MIN_NUMBER
min_temp = MAX_NUMBER
temp = numbers[0]

def operate(n,operation,m):
    if operation==0:
        return n+m
    elif operation==1:
        return n-m
    elif operation==2:
        return n*m
    elif operation==3:
        if n>=0:
            return n//m
        else :
            return -((-n)//m)
        
def dfs(n):
    global temp
    global max_temp
    global min_temp
    if n==N-1:
        max_temp = max(max_temp,temp)
        min_temp = min(min_temp,temp)
    for operation in range(4):
        if operaters[operation]>0:
            before_temp = temp
            temp=operate(temp,operation,numbers[n+1])
            operaters[operation]-=1
            dfs(n+1)
            operaters[operation]+=1
            temp = before_temp
dfs(0)
print(max_temp)
print(min_temp)