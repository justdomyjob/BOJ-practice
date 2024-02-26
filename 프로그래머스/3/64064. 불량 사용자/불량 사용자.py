from collections import defaultdict
from itertools import permutations, combinations

def solution(user_id, banned_id):
    dic = defaultdict(set)
    for index,ban in enumerate(banned_id):
        for user in user_id:
            if check(user,ban):
                dic[index].add(user)
    # init = set()
    init = []
    avail = set()
    def dfs(n,init):
        global ret
        if n == len(banned_id):
            avail.add(frozenset(init))
            return
        else:
            user_list = dic[n]
            for user in user_list:
                if user not in init:
                    init.add(user)
                    dfs(n+1,init)
                    init.remove(user)
    dfs(0,set())
    return len(avail)

def check(user,ban):
    if len(user)!= len(ban):
        return False
    else:
        for u,b in zip(user,ban):
            if b=="*":
                continue
            elif u!=b:
                return False
    return True

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"])