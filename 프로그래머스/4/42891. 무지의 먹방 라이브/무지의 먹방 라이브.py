from collections import Counter

def solution(food_times, k):
    count = dict(Counter(food_times))
    count = sorted(count.items())
    food_count = len(food_times) #현재 food 수
    before = 0
    for time,num in count:
        rotate_time = (time-before) * food_count
        if k-rotate_time >=0:
            k = k-rotate_time
            before = time
            food_count = food_count - num
        else:
            a = k % food_count # 현재 있는 food중에 a번째 선택
            new_food_list = [(i+1,x) for i,x in enumerate(food_times) if x >= time]
            return new_food_list[a][0]
    return -1