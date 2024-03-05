def solution(n, info):
    result = []
    def lion_win(lion):
        l  = 0
        a = 0
        for i in range(11):
            if lion[i] == info[i] == 0:
                continue
            if lion[i] > info[i] :
                l += (10-i)
            else:
                a += (10 - i)
        return l-a
    # print(lion_win([0, 2, 2, 0, 1, 0, 0, 0, 0, 0]))
    ret = []
    global maximum
    maximum = 0
    def dfs(k, lion):
        global maximum
        if k == 11:
            if sum(lion) > n:
                return
            else:
                dif = lion_win(lion)
                if dif > 0:
                    if sum(lion) < n:
                        lion[10] += (n - sum(lion))
                    ret.append([dif,lion[:]])
                    maximum = max(dif,maximum)
        else:
            score = info[k]
            for count in [0,score+1]:
                lion.append(count)
                dfs(k + 1, lion)
                lion.pop()
    dfs(0,[])
    if not ret:
        return [-1]

    ret = [i for i in ret if i[0] == maximum]
    ret.sort(key = lambda x:x[1][::-1])
    print(ret)
    answer = []
    return ret[-1][1]

# solution(5,[2,1,1,1,0,0,0,0,0,0,0])