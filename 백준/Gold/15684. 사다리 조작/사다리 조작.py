def check():
    for i in range(n):
        k = i
        for j in range(h):
            if a[j][k]:
                k += 1
            elif k > 0 and a[j][k-1]:
                k -= 1
        if i != k:
            return False
    return True

def dfs(cnt, x, y):
    global ans
    if check():
        ans = min(ans, cnt)
        return
    elif cnt == 3 or ans <= cnt:
        return
    for i in range(x, h):
        if i == x:
            k = y
        else:
            k = 0
        for j in range(k, n-1):
            if not a[i][j] and not a[i][j+1] and (j == 0 or not a[i][j-1]):
                a[i][j] = True
                dfs(cnt+1, i, j+2)
                a[i][j] = False

n, m, h = map(int, input().split())
a = [[False]*n for _ in range(h)]
ans = 4
for _ in range(m):
    x, y = map(int, input().split())
    a[x-1][y-1] = True
dfs(0, 0, 0)
print(ans if ans < 4 else -1)