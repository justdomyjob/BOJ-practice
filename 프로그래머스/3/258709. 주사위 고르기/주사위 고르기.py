from collections import defaultdict
from itertools import combinations

dp_dice = {}
def solution(dice):
    n = len(dice)
    def get_score_distribution(dice_list): #0,1,2,3,4를 포함한 set
        if dice_list in dp_dice:
            return dp_dice[dice_list]
        if len(dice_list) == 1:
            d = dice_list[0]
            my_dice = dice[d]
            dic = defaultdict(int)
            for i in range(6):
                dic[my_dice[i]]+=1
            dp_dice[dice_list] = dic
        else:
            d1 = dice_list[-1:]
            d2 = dice_list[:-1]
            dic1 = get_score_distribution(d1)
            dic2 = get_score_distribution(d2)
            new_dic3 = defaultdict(int)
            for k2,v2 in dic2.items():
                for k1,v1 in dic1.items():
                    new_dic3[k1+k2] += v1*v2
            dp_dice[dice_list] = new_dic3
        return dp_dice[dice_list]
    a = set([i for i in range(n)])
    maximum = 0
    answer = 0
    for dice_list in combinations(a,n//2):
        d1 = get_score_distribution(dice_list)
        other_dice_list = tuple(a-set(dice_list))
        d2 = get_score_distribution(other_dice_list)
        wins = 0
        for k1,v1 in d1.items():
            for k2, v2 in d2.items():
                if k1>k2:
                    wins += v1*v2
        if wins > maximum:
            maximum = wins
            answer = dice_list
    print(answer)

    ret = []
    for i in answer:
        ret.append(i+1)
    ret.sort()
    return ret
# solution([[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]])
# solution([[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]])