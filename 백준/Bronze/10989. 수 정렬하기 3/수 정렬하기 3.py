import sys

n = int(sys.stdin.readline().rstrip())
#A = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
F = [0 for _ in range(10001)]
for _ in range(n):
    a = int(sys.stdin.readline().rstrip())
    F[a]+=1
for i in range(1,10001):
    F[i] = F[i]+F[i-1]
before =0 
for i in range(1,10001):
    if F[i]==before:
        continue
    else:
        for j in range(F[i]-before):
            print(i)
        before = F[i]
