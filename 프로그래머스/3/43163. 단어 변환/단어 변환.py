from collections import deque
def solution(begin, target, words):
    words.append(begin)
    N = len(words)
    edges = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if can(words[i],words[j]):
                edges[i].append(j)
    begin_index = words.index(begin)
    try:
        target_index = words.index(target)
    except:
        return 0
    visited = [-1] * N
    def bfs(start):
        visited[start] = 0 
        q = deque()
        q.append(start)
        while q:
            v = q.popleft()
            for u in edges[v]:
                if visited[u]==-1:
                    visited[u] = visited[v]+1
                    q.append(u)
    bfs(begin_index)
    if visited[target_index] == -1:
        return 0
    else:
        return visited[target_index]

def can(word_i,word_j):
    count = 0
    for i in range(len(word_i)):
        if word_i[i]==word_j[i]:
            count+=1
    if count==(len(word_i)-1):
        return True
    else:
        return False

    