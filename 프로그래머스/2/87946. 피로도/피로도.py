from itertools import permutations
def solution(k, dungeons):
    length = len(dungeons)
    MAX = 0    
    for order in permutations(dungeons,length):
        hp,count = k,0
        for require, consume in order:
            if hp< require:
                break
            else:
                count+=1
                hp -= consume  
        MAX = max(MAX,count)
    return MAX