import re

while True:
    try:
        line = input()
    except:
        break
    pattern = re.compile('BUG')
    while pattern.findall(line):
        line = re.sub(pattern,"",line)
    print(line)

