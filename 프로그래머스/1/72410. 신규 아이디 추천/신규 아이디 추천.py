def solution(new_id):

    def p1(id):
        return id.lower()

    def p2(id):
        new_id = ""
        for c in id:
            if c in ["-","_","."] or c.isalpha() or c.isdigit():
                new_id+=c
        return new_id

    def p3(id):
        new_id = ""
        before = False
        for c in id:
            if c=="." and before == True:
                continue
            elif c=="." and before == False:
                new_id+=c
                before = True
            else:
                new_id += c
                before = False
        return new_id

    def p4(id):
        if len(id) == 0:
            return id
        if id[0] == ".":
            id = id[1:]
        if len(id) == 0:
            return id
        if id[-1] ==".":
            id = id[:-1]
        return id
    def p5(id):
        if id =="":
            return "a"
        else:
            return id
    def p6(id):
        if len(id)>=16:
            id = id[:15]
        if id[-1] == ".":
            id = id[:-1]
        return id
    def p7(id):
        if len(id)<=2:
            last = id[-1]
            id = id + last * (3-len(id))
        return id
    new_id =  p1(new_id)
    # print(1,new_id)
    new_id =  p2(new_id)
    # print(2,new_id)
    new_id =  p3(new_id)
    # print(3,new_id)
    new_id =  p4(new_id)
    # print(4,new_id)
    new_id =  p5(new_id)
    # print(new_id)
    new_id =  p6(new_id)
    # print(new_id)
    new_id =  p7(new_id)
    # print(new_id)
    return new_id
#
# print(solution("...!@BaT#*..y.abcdefghijklm"))
# # print(solution(	"z-+.^."))
# print(solution("=.="))
# print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution("...!@BaT#*..y.abcdefghijklm"))