try : standard_input = open("input.txt", "r")  
except:pass

def cost(left,right):
    if dp[left][right]!=-1:
        return dp[left][right]
    if left > right:
        print("error")
        exit(0)
    elif left == right:
        return 0
    else:
        min_cost = MAX_COST
        file_size = part_sum(left, right)
        for i in range(left,right):
            temp = cost(left,i) + cost(i+1,right)
            if  temp < min_cost:
                min_cost = temp
        dp[left][right] = min_cost + file_size
        return dp[left][right]

def part_sum(left, right):
    if left>=1:
        file_size = dpsum[right]-dpsum[left-1]
    else:
        file_size = dpsum[right]
    return file_size

n = int(input())
MAX_COST = 1000000000
for _ in range(n):
    K = int(input())
    files = list(map(int,input().split()))
    dp = [[-1 for _ in range(K)] for _ in range(K)]
    dpsum=[0 for _ in range(K)]
    for i in range(K):
        dpsum[i]=dpsum[i-1] + files[i]
    print(cost(0,K-1))