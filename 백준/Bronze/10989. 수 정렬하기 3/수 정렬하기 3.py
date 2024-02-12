n = int(input())

import sys
dic = [0] * 10001
for _ in range(n):
    a = int(sys.stdin.readline().rstrip())
    dic[a] += 1
for i in range(1,10001):
    for j in range(dic[i]):
        print(i)
