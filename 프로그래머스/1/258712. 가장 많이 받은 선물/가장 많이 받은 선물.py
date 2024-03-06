def solution(friends, gifts):
    friends_number = {}
    for i, friend in enumerate(friends):
        friends_number[friend] = i
    graph = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    for ab in gifts:
        a,b = ab.split()
        number1 = friends_number[a]
        number2 = friends_number[b]
        graph[number1][number2] += 1
    index = {}
    for i in range(len(friends)):
        give = sum(graph[i])
        a = [g[i] for g in graph]
        get = sum(a)
        index[i] = give - get
    maximum = 0
    for i in range(len(friends)):
        count = 0
        for j in range(len(friends)):
            if i ==j :
                continue
            else:
                give = graph[i][j]
                get = graph[j][i]
                if give > get :
                    count+=1
                elif give == get:
                    if index[i] > index[j]:
                        count+=1
        maximum = max(maximum,count)
    return maximum

solution(["muzi", "ryan", "frodo", "neo"],["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"])