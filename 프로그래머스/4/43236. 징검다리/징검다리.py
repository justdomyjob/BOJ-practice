def solution(distance, rocks, n):
    
    rocks.sort()
    rocks.append(distance)
 
    
    def check(minimum):
        before = 0 
        remove = 0 
        for rock in rocks:
            if rock - before < minimum:
                remove +=1
            else:
                before = rock
        if remove > n:
            return False
        else:
            return True
    low = 0
    high = distance+1
    while low+1 < high:
        mid = (low+high)//2
        if check(mid):
            low =mid
        else:
            high = mid
    return low

