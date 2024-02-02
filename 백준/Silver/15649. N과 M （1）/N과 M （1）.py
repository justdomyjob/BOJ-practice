N, M = map(int,input().split())

s=[0] * M
def all(n):
    if n == M:
        print(' '.join(map(str,s)))
        return
    for i in range(1,N+1):
        s[n] = i
        if i not in s[:n]:
            all(n+1)
all(0)
