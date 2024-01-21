import sys

n,s = map(int,sys.stdin.readline().rstrip().split())
numbers = list(map(int,sys.stdin.readline().rstrip().split()))

temp = 0
count = 0
end = 0
INF = 10 ** 6
MIN = INF
for start in range(n):
    while temp < s and end < n:
        temp += numbers[end]
        end +=1
    if temp >= s:
        MIN = min(MIN, end-start)
    temp -= numbers[start]
if MIN == INF:
    print(0)
else:
    print(MIN)
