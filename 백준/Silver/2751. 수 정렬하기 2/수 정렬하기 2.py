import sys

n = int(sys.stdin.readline().rstrip())
l = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
l.sort()
for ll in l:
    print(ll)