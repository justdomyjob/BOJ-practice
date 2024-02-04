from collections import deque
def solution(cacheSize, cities):
    ret = 0
    q = deque()
    if cacheSize == 0:
        return 5* len(cities)
    for city in cities:
        city = city.lower()
        if city not in q:
            if q and len(q) == cacheSize:
                q.popleft()
            q.append(city)
            ret+=5
        else:
            q.remove(city)
            q.append(city)
            ret+=1
    return ret