from collections import deque

string = input()

def count(n): #길이가 n인 부분문자열 개수
    ret = 1
    sub = []
    for i in range(len(string)+1-n):
        sub.append(string[i:i+n])
    sub.sort()
    for i in range(1,len(sub)):
        if sub[i]!=sub[i-1]:
            ret+=1
    return ret
sum = 0
for i in range(1,len(string)+1):
    sum += count(i)
print(sum)
