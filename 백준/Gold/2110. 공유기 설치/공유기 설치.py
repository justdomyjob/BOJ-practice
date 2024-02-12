import sys

N,C = map(int,input().split())
homes = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
homes.sort()

def check(n):
    before = homes[0]
    end = homes[-1]
    count =2
    for home in homes[1:-1]:
        if count == C:
            break
        if home -before>=n:
            before = home
            count+=1
    if end - before < n:
        return False
    if count < C:
        return False
    return True

low = 1
end = max(homes)+1
while low + 1 < end:
    mid = (low+end)//2
    if check(mid):
        low = mid
    else:
        end = mid
print(low)