import re
n = int(input())

pattern = re.compile("(100+1+|01)+")
for _ in range(n):
    line = input()
    if pattern.fullmatch(line):
        print("YES")
    else:
        print("NO")
