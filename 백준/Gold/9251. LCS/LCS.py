try : standard_input = open("input.txt", "r")  
except:pass

string1 = input().rstrip()
string2 = input()
len1 = len(string1)
len2 = len(string2)
dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
for i, char1 in enumerate(string1):
    for j, char2 in enumerate(string2):
        if char1==char2:
            dp[i+1][j+1] =dp[i][j] +1
        else:
            dp[i+1][j+1] =max(dp[i+1][j], dp[i][j+1])
print(dp[i+1][j+1])