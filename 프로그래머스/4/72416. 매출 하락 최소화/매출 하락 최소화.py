from collections import defaultdict

def solution(sales, links):
    tree={}
    for i,data in enumerate(sales):
        tree[i+1] = Node(data)
    for a,b in links:
        tree[a].add_child(b)

    dp = {}
    INF = 10**7
    def rec(i,j):
        if (i,j) in dp:
            return dp[(i, j)]
        else:
            child = tree[i].child
            if len(child) == 0:
                if j==0:
                    dp[(i,j)] = 0
                else:
                    dp[(i,j)] = tree[i].value
            else:
                sum_child = 0
                count_cilld = 0 #참석하는 자식 수
                minimum_child = INF #가장 적게 버는 자식의 차이
                for ch in child:
                    yes = rec(ch,1)
                    no = rec(ch,0)
                    if yes <= no :
                        count_cilld +=1
                    minimum_child = min(minimum_child,yes-no)
                    sum_child += min(yes,no)

                if j == 1: #부모가 참석함
                    dp[(i, j)] = sum_child + tree[i].value
                else: #부모 참석 안함
                    if count_cilld == 0 :
                        sum_child += minimum_child
                    dp[(i,j)] = sum_child
        return dp[(i,j)]


    answer = 0
    return min(rec(1,1),rec(1,0))

class Node:
    def __init__(self, value, child=None):
        if child is None:
            child = []
        self.value =value
        self.child = child
    def add_child(self, value):
        self.child.append(value)
    def __repr__(self):
        return "data is " + str(self.value) + "  child is  " +  str(self.child)
# sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
# links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
# solution(sales,links)