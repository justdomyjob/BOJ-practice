n = int(input())
numbers = list(map(int,input().split()))
a = set(numbers)
b = list(a)
b.sort()
dic = {}

for i in range(len(b)):
    dic[b[i]] = i

for num in numbers:
    print(dic[num], end = " ")