import sys
from itertools import combinations

N, M = map(int,sys.stdin.readline().rstrip().split())
city = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]
home = []
chiken = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append((i,j))
        elif city[i][j] == 2:
            chiken.append((i,j))
home_chikein_distance = [[] for _ in range(len(home))]
for i,(homy,homx) in enumerate(home):
    for chiy, chix in chiken:
        d = abs(chix-homx) + abs(chiy-homy)
        home_chikein_distance[i].append(d)

home_sum = [sum(x) for x in home_chikein_distance]

chi_list = [i for i in range(len(chiken))]

chiMList = list(combinations(chi_list,M))


MIN = 10**9
for chiM in chiMList:
    # print("chiM = ", chiM)
    sum = 0
    for home_chiken in home_chikein_distance:
        # print("home_chiken = ", home_chiken)
        new_chi = []
        for chi in chiM:
            new_chi.append(home_chiken[chi])
        # print("new_chi = ", new_chi)
        sum += min(new_chi)
    # print("sum = ", sum)
    if sum < MIN:
        MIN = sum
print(MIN)
