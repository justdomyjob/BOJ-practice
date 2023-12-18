try : standard_input = open("input.txt", "r")  
except:pass
import copy
N, K = map(int,input().split())
W_V = [list(map(int,input().split())) for _ in range(N)]
dp = {0:0}
for W,V in W_V:
    dp2 = copy.deepcopy(dp)
    for key in dp2:
        if key+W >K:
            continue
        dp[key+W]=max(dp2[key]+V,dp2.get(key+W,0))
print(max(dp.values()))