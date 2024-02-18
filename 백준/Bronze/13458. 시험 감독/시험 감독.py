N = int(input())
Ai = list(map(int,input().split()))
B,C = map(int,input().split())
ret = 0
for A in Ai:
    A-= B
    ret+=1
    if A<0:
        continue
    elif A%C==0:
        ret+= A//C
    else:
        ret+=A//C+1
print(ret)