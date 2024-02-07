def solution(arr):
    numbers = [int(i) for i in arr if i.isdigit()]
    operations = [i for i in arr if not i.isdigit()]
    # print(numbers)
    # print(operations)
    length = len(numbers)
    dp = [[[] for _ in range(length)] for _ in range(length)] #dp[0][2] : 0번째에서 2번째까지 계산한 값
    for i in range(length):
        dp[i][i].append(numbers[i])
    for i in range(1,length):
        for j in range(length-i):
            for k in range(j,j+i):  #dp[j][j+i] = dp[j][k] * dp[k+1][j+i]
                for value1 in dp[j][k]:
                    for value2 in dp[k+1][j+i]:
                        if operations[k] == "-":
                            dp[j][j+i].append(value1-value2)
                        else:
                            dp[j][j+i].append(value1+value2)
            m = min(dp[j][j+i])
            M = max(dp[j][j+i])
            dp[j][j+i] = [m, M]
    # for d in dp:
    #     print(*d)
    return max(dp[0][length-1])