import sys

input = sys.stdin.readline
n = int(input())
numbers = list(map(int,input().split()))
s = int(input())

dic = {}
count = 0
for num in numbers:
    count+=dic.get(num,0)
    dic[s-num] = dic.get(s-num,0) + 1
print(count)
