import sys
from collections import Counter

N, M = map(int, sys.stdin.readline().rstrip().split())
words = []
for _ in range(N):
    words.append(sys.stdin.readline().rstrip())
counter = Counter(words)
listCounter = counter.most_common()
listCounter.sort(key = lambda x : (-x[1],-len(x[0]),x) )

for word,count in listCounter:
    if len(word) < M:
        continue
    print(word)

