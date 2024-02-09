import sys
sys.setrecursionlimit(10**5)
count = 0 
def solution(numbers, target):
    def dfs(n,s):
        global count
        if n==len(numbers):
            if s == target:
                count+=1
                return
        else:
            plus = s + numbers[n]
            minus = s - numbers[n]
            dfs(n+1,plus)
            dfs(n+1,minus)
    dfs(0,0)
    return count