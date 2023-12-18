try : standard_input = open("input.txt", "r")  
except:pass

n = int(input())
num_list = list(map(int,input().split()))
num_list2 = num_list[::-1]

dp1 = [0 for _ in range(n)]
dp1[0] = 1

for i in range(1,n):
    temp = 1
    for j in range(i):
        if num_list[i] > num_list[j] and temp < dp1[j] + 1:
            temp = dp1[j] +1
    dp1[i] = temp

dp2 = [0 for _ in range(n)]
dp2[0] = 1

for i in range(1,n):
    temp = 1
    for j in range(i):
        if num_list2[i] > num_list2[j] and temp < dp2[j] + 1:
            temp = dp2[j] +1
    dp2[i] = temp
dp2 = dp2[::-1]
dp3 = [a+b for a,b in zip(dp1,dp2)]
print(max(dp3)-1)