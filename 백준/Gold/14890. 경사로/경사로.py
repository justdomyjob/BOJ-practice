N,L = map(int,input().split())
row = [list(map(int,input().split())) for _ in range(N)]
# col[0] = [row[0][0], row[1][0],...]
#
# col[i] = [row[0][i], row[1][i], row[2][i]
# col[i] = [row[j][i] for j in range(N)]
col = [[row[j][i] for j in range(N)] for i in range(N)]

def all_same(l):
    for c in l:
        if c!=l[0]:
            return False
    return True

def check(line):
    before = line[0]
    seq =1
    i = 1
    while 0<=i<N:
        if line[i]==before:
            seq+=1
        else:
            if abs(line[i] - before) >1:
                return 0
            else:
                if line[i] - before ==1: #높아짐
                    if seq <L:
                        return 0
                    else:
                        before = line[i]
                        seq=1
                elif before - line[i] == 1: #낮아짐
                    if i+L>N :
                        return 0
                    else:
                        if all_same(line[i:i+L]):
                            before = line[i+L-1]
                            i+=(L-1)
                            seq=0
                        else:
                            return 0
        i+=1
    return 1

ans = 0
for g in row:
    ans += check(g)
for g in col:
    ans += check(g)
print(ans)