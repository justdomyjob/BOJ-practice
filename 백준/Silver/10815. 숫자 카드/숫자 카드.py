import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int,input().split()))
m = int(input())
numbers2 = list(map(int,input().split()))

dic = {}
for num in numbers:
    dic[num] = 1
for num2 in numbers2:
    if num2 in dic:
        print(1, end = " ")
    else:
        print(0, end = " ")