def solution(s):
    dic = {}
    dic2 = {}
    dic[0] = 'zero'
    dic[1] = 'one'
    dic[2] = 'two'
    dic[3] = 'three'
    dic[4] = 'four'
    dic[5] = 'five'
    dic[6] = 'six'
    dic[7] = 'seven'
    dic[8] = 'eight'
    dic[9] = 'nine'
    for i in range(10):
        dic2[dic[i]] = i
    answer = ""
    for char in s:
        if char.isdigit():
            answer+=dic[int(char)]
        else:
            answer+=char
    ret = ""
    before = 0
    print(answer)
    for i in range(len(answer)):
        print(answer[before:i])
        if answer[before:i+1] in dic2:
            ret+=str(dic2[answer[before:i+1]])
            before = i+1
    print(ret)
            
    return int(ret)