from collections import defaultdict


def solution(commands):
    graph = [["EMPTY" for _ in range(51)] for _ in range(51)]
    parent = {}
    answer = []
    def find_parent(r1,c1):
        if (r1,c1) not in parent:
            parent[(r1,c1)] = (r1,c1)
        if parent[(r1,c1)] != (r1,c1):
            parent[(r1,c1)] = find_parent(*parent[(r1,c1)])
        return parent[(r1,c1)]

    def union(r1,c1,r2,c2):
        (r1,c1) = find_parent(r1,c1)
        (r2,c2) = find_parent(r2,c2)
        if r1<r2:
            parent[(r2,c2)] = parent[(r1,c1)]
        elif r1>r2:
            parent[(r1, c1)] = parent[(r2, c2)]
        else:
            if c1<=c2:
                parent[(r2,c2)] = parent[(r1,c1)]
            else:
                parent[(r1, c1)] = parent[(r2, c2)]
    for command in commands:
        splited = command.split()
        if splited[0] == "UPDATE":
            if len(splited)==4:
                r,c,value = int(splited[1]),int(splited[2]),splited[3]
                for i in range(51):
                    for j in range(51):
                        if find_parent(i,j) == find_parent(r,c):
                            graph[i][j] = value
            else:
                v1,v2 = splited[1],splited[2]
                for i in range(51):
                    for j in range(51):
                        if graph[i][j] == v1:
                            graph[i][j] = v2

        elif splited[0] == "MERGE":
            r1,c1,r2,c2 = int(splited[1]),int(splited[2]),int(splited[3]),int(splited[4])
            v1,v2 = graph[r1][c1],graph[r2][c2]
            if r1==r2 and c1==c2:
                continue
            else:
                union(r1, c1, r2, c2)
                if v1=="EMPTY" and v2!="EMPTY":
                    for i in range(51):
                        for j in range(51):
                            if find_parent(i,j) == find_parent(r1,c1):
                                graph[i][j] = v2
                else:
                    for i in range(51):
                        for j in range(51):
                            if find_parent(i,j) == find_parent(r1,c1):
                                graph[i][j] = v1

        elif splited[0] == "UNMERGE":
            r1,c1 = int(splited[1]),int(splited[2])
            v1 = graph[r1][c1]
            ret = []
            for i in range(51):
                for j in range(51):
                    if find_parent(i,j) == find_parent(r1,c1):
                        graph[i][j] = "EMPTY"
                        ret.append((i,j))
            for i,j in ret:
                parent[(i,j)] = (i,j)
            graph[r1][c1] = v1

        elif splited[0] == "PRINT":
            r,c = int(splited[1]),int(splited[2])
            answer.append(graph[r][c])

        # for g in graph[:3]:
        #     print(g[:3])
        # print()
    print(answer)
    return answer





# solution(["UPDATE 1 1 menu", "UPDATE 1 2 category","MERGE 1 1 1 2", "UNMERGE 1 1", "PRINT 1 1"])
solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"])
# solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"])