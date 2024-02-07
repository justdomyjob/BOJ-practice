def solution(arr):
    numbers = [int(i) for i in arr if i.isdigit()]
    operations = [i for i in arr if not i.isdigit()]
    length = len(numbers)
    dp = [[[] for _ in range(length)] for _ in range(length)] #dp[0][2] : 0번째에서 2번째까지 계산한 값
    for i in range(length):
        dp[i][i].append(numbers[i])
        dp[i][i].append(numbers[i])
    for i in range(1,length):
        for j in range(length-i):
            for k in range(j,j+i):  
                m1,M1 = dp[j][k]
                m2,M2 = dp[k+1][j+i]
                if operations[k] == "-":
                    dp[j][j+i].append(m1-m2)
                    dp[j][j+i].append(m1-M2)
                    dp[j][j+i].append(M1-m2)
                    dp[j][j+i].append(M1-M2)
                else:
                    dp[j][j+i].append(m1+m2)
                    dp[j][j+i].append(m1+M2)
                    dp[j][j+i].append(M1+m2)
                    dp[j][j+i].append(M1+M2)
            m = min(dp[j][j+i])
            M = max(dp[j][j+i])
            dp[j][j+i] = [m,M]
    return max(dp[0][length-1])