try : standard_input = open("input.txt", "r")  
except:pass

n = int(input())
a=0
b=0
def fib(n):
    if n==1 or n==2:
        global a
        a+=1
        return 1  
    else:
        return fib(n-1)+fib(n-2)

dp = [0]*(n+1)

def fibo(n):
    dp[1]=1
    dp[2]=1
    for i in range(3,n+1):
        global b
        b+=1
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]
fib(n)
fibo(n)
print(a,b)