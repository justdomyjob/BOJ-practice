import sys

N = int(input())
numbers = list(map(int,sys.stdin.readline().rstrip().split()))
operators = list(map(int,sys.stdin.readline().rstrip().split()))

MAX = -10**9
MIN = -MAX

value = numbers[0]
def dfs(n):
    global value, MAX, MIN
    if n == N:
        if value > MAX:
            MAX = value
        if value < MIN:
            MIN = value
    for i in range(4):
        if operators[i] > 0:
            temp = value
            operators[i] -= 1
            operation(i,n)
            dfs(n+1)
            operators[i] += 1
            value = temp

def operation(i,n):
    global value
    if i == 0:
        value += numbers[n]
    elif i == 1:
        value -= numbers[n]
    elif i == 2:
        value *= numbers[n]
    elif i == 3:
        if value > 0 :
            value = value // numbers[n]
        else :
            value = -((-value) // numbers[n])
dfs(1)
print(MAX)
print(MIN)
