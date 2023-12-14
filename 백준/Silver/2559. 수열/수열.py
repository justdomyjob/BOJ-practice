try : standard_input = open("input.txt", "r")  
except:pass

N, K = map(int,input().split())
temperture = list(map(int,input().split()))

sum = [sum(temperture[:K])]
for i in range(K,N):
    sum.append(sum[-1]+temperture[i]-temperture[i-K])
print(max(sum))