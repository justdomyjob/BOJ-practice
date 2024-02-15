import copy
import sys
sys.setrecursionlimit(10**6)
def solution(key, lock):
    N = len(lock)
    M = len(key)
    new_key = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(M):
        for j in range(M):
            new_key[i][j] = key[i][j]
    key1 = rotate(new_key)
    key2 = rotate(key1)
    key3 = rotate(key2)
    keys = [new_key,key1,key2,key3]
    for k in keys:
        temp = copy.deepcopy(lock)
        if check(k,temp):
            return True
        else:
            continue
    return False

def check(key,lock):
    N = len(lock)
    dolgi = find_left_top(key)
    lr, lc = find_left_top_lock(lock)
    if lr==100:
        return True
    for kr,kc in dolgi:
        temp_lock = copy.deepcopy(lock)
        temp_key = move(key, lr - kr, lc - kc)
        flag = False
        for i in range(N):
            for j in range(N):
                if temp_key[i][j] ==1:
                    if temp_lock[i][j] ==0 :
                        temp_lock[i][j] =1
                    else:
                        flag =True
                        break
            if flag:
                break
        if flag:
            continue
        for i in range(N):
            for j in range(N):
                if temp_lock[i][j] == 0:
                    flag = True
                    break
            if flag:
                break
        if flag:
            continue
        return True

def rotate(key):
    N = len(key)
    new_key = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_key[i][j] = key[N-1-j][i]
    return new_key

def move(key,r,c):
    N = len(key)
    new_key = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if 0<=i-r<N and 0<=j-c<N:
                new_key[i][j] = key[i-r][j-c]
    return new_key

def find_left_top(graph):
    r = len(graph)
    c = len(graph[0])
    ret = []
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 1:
                ret.append((i,j))
    return ret


def find_left_top_lock(graph):
    r = len(graph)
    c = len(graph[0])
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 0:
                return i,j
    return 100,100