from itertools import product


def solution(users, emoticons):
    length = len(emoticons)
    discount_list = [10,20,30,40]
    a = product(discount_list,repeat = length)
    maximum_user = 0
    maximum_price = 0
    ret =[]
    for dis_list in a:
        buy_user = 0
        sum_price = 0
        for user_dis, user_price in users:
            buy = 0
            for emo_dis,emo_price in zip(dis_list,emoticons):
                if user_dis<= emo_dis:
                    buy += emo_price * (100-emo_dis)//100
            if buy >= user_price:
                buy_user+=1
            else:
                sum_price+=buy
        if buy_user == maximum_user:
            maximum_price = max(maximum_price,sum_price)
        elif buy_user > maximum_user:
            maximum_user = buy_user
            maximum_price = sum_price

    return [maximum_user,maximum_price]

solution(	[[40, 10000], [25, 10000]], [7000, 9000])
# solution( [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900])