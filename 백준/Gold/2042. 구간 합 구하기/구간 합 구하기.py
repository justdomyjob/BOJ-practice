
def prefix_sum(i):
    ret = 0
    while i>0:
        ret += tree[i]
        i -= (i&-i)
    return ret

def update(i,dif):
    while i <=N:
        tree[i] +=dif
        i+=(i&-i)

def interval_sum(start,end):
    return prefix_sum(end) - prefix_sum(start-1)

N,M,K = map(int,input().split())
arr = [0] *(N+1)
tree = [0] *(N+1)

for i in range(1,N+1):
    a = int(input())
    arr[i] = a
    update(i,a)

for i in range(M+K):
    a,b,c = map(int,input().split())
    if a ==1:
        update(b,c-arr[b])
        arr[b] = c
    else:
        print(interval_sum(b,c))