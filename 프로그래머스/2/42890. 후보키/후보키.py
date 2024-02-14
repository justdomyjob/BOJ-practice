from itertools import combinations
def solution(relation):

    row = len(relation)
    col = len(relation[0])
    col_list = [i for i in range(col)]

    def check(col_num):
        ret = []
        a = combinations(col_list,col_num)
        for comb in a:
            already = False
            for p in possible:
                if p.issubset(set(comb)):
                    already = True
                    break
            if already:
                continue
            key = True
            new_rows = []
            for each_row in relation:
                new_row =[]
                for col in comb:
                    new_row.append(each_row[col])
                new_rows.append(new_row)
            new_rows.sort()
            for i in range(1,len(new_rows)):
                if new_rows[i-1] == new_rows[i]:
                    key = False
                    break
            if key==True:
                ret.append(set(comb))
        return ret
    possible = []
    for i in range(1,col+1):
        temp = check(i)
        possible.extend(temp)
    # print(possible)
    return len(possible)









relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))
# print({0,1}.issubset({0,1,2}))
# print(set((0,)))