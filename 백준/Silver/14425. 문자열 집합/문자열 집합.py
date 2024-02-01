import sys

input = sys.stdin.readline
n,m = map(int,input().split())
dic = {}

for _ in range(n):
    dic[input()] = 1

count = 0
for _ in range(m):
    if input() in dic:
        count+=1
print(count)