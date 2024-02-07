def solution(money):
    def re(start,end): #첫집과 마지막집은 연결된게 아님
        if dp[start][end]!=-1:
            return dp[start][end]
        elif start==end:
            dp[start][end] = money[start]
        elif start+1==end:
            value = max(money[start], money[end])
            dp[start][end] = value
        else:
            value1 = money[start] + re(start+2,end)
            value2 = re(start+1,end)
            value = max(value1,value2)
            dp[start][end] = value
        return dp[start][end]
        
    length = len(money)
    dp = [[-1 for _ in range(length)] for _ in range(length)] 
    a = re(1,length-1)
    b = re(2,length-2) + money[0]
    
    return max(a,b)
