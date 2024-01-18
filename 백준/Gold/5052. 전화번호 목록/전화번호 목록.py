import sys

test = int(input())
for _ in range(test):
    flag = False
    n = int(sys.stdin.readline().rstrip())
    call = [sys.stdin.readline().rstrip() for _ in range(n)]
    call.sort()
    MIN = len(call[0])
    for i in range(1,len(call)):
        if call[i-1] == call[i][:len(call[i-1])]:
            print("NO")
            flag = True
            break
    if flag:
        continue
    else:
        print("YES")

