import heapq
def solution(jobs):
    q = []
    temp = []
    finish_time = 0
    wait_time = 0
    for arrival, take in jobs:
        heapq.heappush(q, (arrival,take))
    while q:
        while q and q[0][0] <= finish_time:
            arrival, take = heapq.heappop(q)
            heapq.heappush(temp,(take,arrival))
        if not temp:
            finish_time = q[0][0]
            continue
        take, arrival = heapq.heappop(temp)
        finish_time += take
        wait_time += finish_time - arrival
        while temp:
            take, arrival = heapq.heappop(temp)
            heapq.heappush(q,(arrival,take))
    return wait_time//len(jobs)