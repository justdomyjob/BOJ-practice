# import sys
#
# input = sys.stdin.readline
a = input()
length = len(a)
total = set()
for l in range(1,length+1):
    for i in range(length+1-l):
        total.add(a[i:i+l])
print(len(total))
