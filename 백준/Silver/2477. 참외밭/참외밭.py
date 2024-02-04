n = int(input())
edges = [list(map(int,input().split()))[1] for _ in range(6)]

edges1 = [edges[i] for i in range(6) if i%2==0]
edges2 = [edges[i] for i in range(6) if i%2==1]
m1 = max(edges1)
m2 = max(edges2)
i1 = (edges.index(m1) + 3)%6
i2 = (edges.index(m2) + 3)%6

print((m1*m2 - edges[i1]*edges[i2])*n)