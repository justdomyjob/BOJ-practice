from itertools import product
def solution(word):
    data = ["A","E","I","O","U"]
    words =[]
    for i in range(1,6):
        result = product(data, repeat=i)
        for w in result:
            words.append("".join(w))
    words.sort()
    return words.index(word)+1