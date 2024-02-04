from collections import deque
import sys
sys.setrecursionlimit(10**5)
def solution(files):
    answer = []
    files.sort(key = lambda x: (get_head(x), get_number(x)))
    print(files)
    return files

def get_head(file):
    for i in range(len(file)):
        if file[i].isdigit():
            return file[:i].lower()

def get_number(file):
    for i in range(len(file)):
        if file[i].isdigit():
            start = i
            break
    for i in range(start,len(file)):
        if not file[i].isdigit():
            if i-start > 5:
                return int(file[start:start+5])
            return int(file[start:i])
    return int(file[start:])