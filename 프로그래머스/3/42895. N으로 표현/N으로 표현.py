
def solution(N, number):
    nnn = [int(str(N)*i) if i>0 else None for i in range(9)]
    dp = [None,set({N}), set({nnn[2]}), set({nnn[3]}), set({nnn[4]}), set({nnn[5]}), set({nnn[6]}), set({nnn[7]}), set({nnn[8]})]
    # print(dp)
    for i in range(2,9):  #555같은거 따로 연산한것들
        for j in range(1,i):
            before = dp[i-j]
            after = dp[j]
            for num1 in before:
                for num2 in after:
                    dp[i].add(num1+num2)
                    dp[i].add(num1-num2)
                    dp[i].add(num1*num2)
                    if num2!=0:
                        dp[i].add(num1/num2)
    # print(dp)
    for i in range(1,9):
        if number in dp[i]:
            return i
    return -1