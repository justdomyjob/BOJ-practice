import bisect


def solution(info, query):
    graph = [[[[[] for _ in range(3)] for _ in range(3)] for _ in range(3)] for _ in range(4)]

    dic1 = {"-":0,"java" : 1, "cpp" : 2, "python" :3}
    dic2 = {"-":0,"backend" : 1, "frontend":2}
    dic3 = {"-":0,"junior" : 1, "senior" : 2}
    dic4 = {"-":0,"chicken" : 1, "pizza" : 2}
    for i in info:
        a= i.split()
        for j1 in [0,dic1[a[0]]]:
            for j2 in [0, dic2[a[1]]]:
                for j3 in [0, dic3[a[2]]]:
                    for j4 in [0, dic4[a[3]]]:
                        graph[j1][j2][j3][j4].append(int(a[4]))
    for i1 in range(4):
        for i2 in range(3):
            for i3 in range(3):
                for i4 in range(3):
                    graph[i1][i2][i3][i4].sort()
    # print(graph)
    ret = []
    for q in query:
        a = q.split(" and ")
        b = a[3].split()
        a = a[:3]
        a.extend(b)
        find_list = graph[dic1[a[0]]][dic2[a[1]]][dic3[a[2]]][dic4[a[3]]]
        index = len(find_list)-bisect.bisect_left(find_list,int(a[4]))
        ret.append(index)
    return ret