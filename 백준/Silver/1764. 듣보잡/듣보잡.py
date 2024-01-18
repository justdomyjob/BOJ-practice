import bisect
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
dd = []
bb = []
for _ in range(n):
    dd.append(sys.stdin.readline().rstrip())

dd.sort()
for _ in range(m):
    b = sys.stdin.readline().rstrip()
    if bisect.bisect_left(dd,b) < len(dd) and dd[bisect.bisect_left(dd,b)]==b:
        bb.append(b)
bb.sort()

print(len(bb))
for b in bb:
    print(b)

