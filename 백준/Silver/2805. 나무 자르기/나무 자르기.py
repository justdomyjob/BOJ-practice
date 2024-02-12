N,M = map(int,input().split())
trees = list(map(int,input().split()))

def check(n):
    count = 0
    for tree in trees:
        if tree >= n:
            count+= (tree-n)
    if count>=M:
        return True
    else:
        return False

low = 0
end = max(trees)
while low + 1 < end:
    mid = (low+end)//2
    if check(mid):
        low = mid
    else:
        end = mid
print(low)