try : standard_input = open("input.txt", "r")  
except:pass

N, M = map(int,input().split())
A = list(map(int,input().split()))

accum_sum = []
for a in A:
    try:
        accum_sum.append(accum_sum[-1]+a)
    except:
        accum_sum.append(a)

remainder = [0 for _ in range(M)] 
for sum in accum_sum:
    remainder[sum%M] +=1

ans = remainder[0]
for r in remainder:
    ans += r*(r-1)//2
print(ans)
