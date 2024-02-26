def solution(s):
    dic = {}

    s = s.split("},{")
    s[0] = s[0][2:]
    s[-1] = s[-1][:-2]
    for i in range(len(s)):
        a = s[i].split(",")
        s[i] = set(a)
    for ss in s:
        dic[len(ss)] = ss
    a = [int(list(dic[1])[0])]
    for i in range(2,len(s)+1):
        b = dic[i] - dic[i-1]
        b = int(list(b)[0])
        a.append(b)

    return a