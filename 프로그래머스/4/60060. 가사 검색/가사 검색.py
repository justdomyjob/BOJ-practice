import bisect

array= [[] for _ in range(10001)]
reversed_array= [[] for _ in range(10001)]

def solution(words, queries):
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])
    for a in array:
        a.sort()
    for b in reversed_array:
        b.sort()

    ret = []
    for query in queries:
        if query[0]=="?":
            ret.append(count_between(reversed_array,query[::-1]))
        else:
            ret.append(count_between(array,query))
    return  ret

def count_between(array,query):
    temp1 = query.replace("?", "a")
    temp2 = query.replace("?", "z")
    a = bisect.bisect_left(array[len(query)], temp1)
    b = bisect.bisect_right(array[len(query)], temp2)
    c = b - a
    return c