from collections import Counter

def solution(N, stages):
    count = dict(Counter(stages))
    print(count)
    players = len(stages)
    dic = {}
    for i in range(1,N+1):
        if players!=0:
            dic[i] = count.get(i,0) / players
        else:
            dic[i] = 0
        players -= count.get(i,0)
    a = list(dic.items())
    a.sort(key = lambda x:-x[1])
    b = [x for x,y in a]
    return b

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))