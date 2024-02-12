def solution(n, times):
    def check(minutes):
        count = 0
        for time in times:
            count += minutes//time
        if count >=n:
            return True
        else:
             return False
    low = 0
    high = max(times)*n+1
    while low+1<high:
        mid = (low+high)//2
        if check(mid):
            high = mid
        else:
            low = mid
    return high
    


