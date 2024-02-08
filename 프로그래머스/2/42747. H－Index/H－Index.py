from bisect import bisect_left,bisect_right
def solution(citations):
    citations.sort()
    answer = []
    for h in range(1001,-1,-1):
        bigger_or_equal = len(citations)- bisect_left(citations,h)
        if bigger_or_equal>= h:
            return h
    return 0