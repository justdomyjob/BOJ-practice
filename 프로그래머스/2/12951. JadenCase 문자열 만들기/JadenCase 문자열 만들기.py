def solution(s):
    s= s.split(" ")
    newlist = []
    for word in s:
        print(word)
        if word=="":
            newlist.append(word)
        elif word[0] in [0,1,2,3,4,5,6,7,8,9]:
            newlist.append(word)
        else:
            word = word.capitalize()
            newlist.append(word)
    answer = " ".join(newlist)
    return answer