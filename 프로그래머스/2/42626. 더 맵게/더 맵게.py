import heapq
def solution(scoville, K):
    q = []
    for s in scoville:
        heapq.heappush(q,s)
    count = 0
    while q[0] < K:
        a =heapq.heappop(q)
        b =heapq.heappop(q)
        c = a+2*b
        heapq.heappush(q,c)
        count+=1
        if len(q) ==1 and c<K:
            return -1
    return count