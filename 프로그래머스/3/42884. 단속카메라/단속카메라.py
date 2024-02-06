def solution(routes):
    routes.sort(key = lambda x:x[1])
    count = 1
    temp = routes[0][1]
    print(routes)
    for start, end in routes[1:]:
        if start > temp:
            temp = end
            count+=1
        else:
            continue
    return count