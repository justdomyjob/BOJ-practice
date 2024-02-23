from collections import defaultdict
from itertools import combinations


def solution(orders, course):
    ret = []
    for count in course:
        dic = defaultdict(int)
        for order in orders:
            order_list = list(order)
            a = combinations(order_list,count)
            for each in a:
                each = list(each)
                each.sort()
                string =""
                for e in each:
                    string+=e
                dic[string]+= 1
        items = list(dic.items())
        items.sort(key = lambda x:-x[1])
        
        if items:
            maximum = items[0][1]
            if maximum <2:
                continue
            for menu, count in items:
                if count == maximum:
                    ret.append(menu)
    ret.sort()

    answer = []
    return ret