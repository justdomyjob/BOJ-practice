import sys

input = sys.stdin.readline

n = int(input())
s= set()
for _ in range(n):
    op = sys.stdin.readline().rstrip().split()
    if op[0] == "all":
       s= set([i for i in range(1,21)])
    elif op[0] == "empty":
        s = set()
    elif op[0] == "add":
        s.add(int(op[1]))
    elif op[0] == "remove":
        try:
            s.remove(int(op[1]))
        except:
            continue
    elif op[0] == "check":
        if int(op[1]) in s:
            print(1)
        else:
            print(0)
    elif op[0] == "toggle":
        if int(op[1]) in s:
            s.remove(int(op[1]))
        else:
            s.add(int(op[1]))
