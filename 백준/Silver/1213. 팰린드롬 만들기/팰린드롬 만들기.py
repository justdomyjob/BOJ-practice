from collections import Counter

string = input()
counter = Counter(string)


oddCount = 0
for key in counter:
    if counter[key]%2==1:
        oddCount+=1
        oddChar = key

if oddCount>1:
    print("I'm Sorry Hansoo")
    exit(0)

ret = [0] * len(string)
keyList = list(counter.keys())
keyList.sort()

def fill():
    i = 0
    for key in keyList:
        while counter[key] > 0:
            ret[i] = key
            ret[-(i + 1)] = key
            counter[key] -= 2
            i += 1
if oddCount == 1:
    ret[len(string)//2] = oddChar
    counter[oddChar] -= 1
    fill()
else:
    fill()
print("".join(ret))

