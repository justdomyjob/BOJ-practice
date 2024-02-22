n,M, k = map(int,input().split())
fires = [list(map(int,input().split())) for _ in range(M)]

graph = [[[] for _ in range(n)] for _ in range(n)]

dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,1,1,1,0,-1,-1,-1]

for r,c,m,s,d in fires:
    graph[r-1][c-1].append((m,s,d))

def p():
    for g in graph:
        print(g)
    print()


def command():
    new_graph = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            while graph[i][j]:
                m,s,d = graph[i][j].pop()
                ni = (i + dy[d] * s) %n
                nj = (j + dx[d] * s) %n
                new_graph[ni][nj].append((m,s,d))
    for i in range(n):
        for j in range(n):
            if new_graph[i][j]:
                if len(new_graph[i][j]) > 1:
                    first_even_odd = new_graph[i][j][0][2] % 2
                    even = True
                    nm = 0
                    ns = 0

                    for m,s,d in new_graph[i][j]:
                        nm+=m
                        ns+=s
                        if d%2!=first_even_odd:
                            even = False
                    nm = nm//5
                    if nm == 0:
                        continue
                    ns = ns//len(new_graph[i][j])
                    if even:
                        graph[i][j].append((nm,ns,0))
                        graph[i][j].append((nm, ns, 2))
                        graph[i][j].append((nm, ns, 4))
                        graph[i][j].append((nm, ns, 6))
                    else:
                        graph[i][j].append((nm, ns, 1))
                        graph[i][j].append((nm, ns, 3))
                        graph[i][j].append((nm, ns, 5))
                        graph[i][j].append((nm, ns, 7))
                else:
                    graph[i][j].append(new_graph[i][j][0])
for _ in range(k):
    command()

ret = 0
for i in range(n):
    for j in range(n):
        for m,s,d in graph[i][j]:
            ret +=m
print(ret)


