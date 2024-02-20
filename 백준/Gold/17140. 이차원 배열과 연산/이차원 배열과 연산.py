from collections import defaultdict

r,c,k = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(3)]

def check():
    try:
        if graph[r-1][c-1] == k:
            return True
    except:
        return False
def pp():
    for g in graph:
        print(g)
    print()

def row_sort():
    global graph
    new_graph = []
    max_line_length = 0
    for line in graph:
        new_line = []
        dic = defaultdict(int)
        for num in line:
            if num ==0:
                continue
            dic[num] +=1

        items = sorted(list(dic.items()), key=lambda x: (x[1], x[0]))
        for i,count in items:
            new_line.extend([i,count])
        new_line = new_line[:100]
        max_line_length = max(len(new_line), max_line_length)
        new_graph.append(new_line)
    for line in new_graph:
        require = max_line_length - len(line)
        line = line.extend([0] * require)
    graph = new_graph

# def column_to_row(): #(R*C) -> (C*R)
#     R = len(graph)
#     C = len(graph[0])

def column_sort():
    global graph
    R = len(graph)
    C = len((graph[0]))
    new_graph = []
    max_line_length = 0
    temp_graph = [[graph[i][j] for i in range(R)] for j in range(C)]

    for line in temp_graph:
        new_line = []
        dic = defaultdict(int)
        for num in line:
            if num == 0:
                continue
            dic[num] += 1
        items = sorted(list(dic.items()), key=lambda x: (x[1], x[0]))
        for i, count in items:
            new_line.extend([i, count])
        new_line = new_line[:100]
        max_line_length = max(len(new_line), max_line_length)
        new_graph.append(new_line)
    for line in new_graph:
        require = max_line_length - len(line)
        line = line.extend([0] * require)
    temp_R = len(new_graph)
    temp_C = len(new_graph[0])
    graph = [[new_graph[i][j] for i in range(temp_R)] for j in range(temp_C)]

for i in range(101):
    if check():
        print(i)
        exit(0)
    R = len(graph)
    C = len(graph[0])
    if R>=C:
        row_sort()
    else:
        column_sort()

print(-1)
