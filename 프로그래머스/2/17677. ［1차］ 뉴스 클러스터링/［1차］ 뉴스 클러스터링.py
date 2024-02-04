def solution(str1, str2):
    str1=str1.lower()
    str2=str2.lower()
    dic1 = {}
    dic2 = {}
    for i in range(len(str1)-1):
        if ord("a")<=ord(str1[i])<=ord("z") and ord("a")<=ord(str1[i+1])<=ord("z"):
            pair = str1[i:i+2]
            dic1[pair] = dic1.get(pair,0)+1
    for i in range(len(str2)-1):
        if ord("a")<=ord(str2[i])<=ord("z") and ord("a")<=ord(str2[i+1])<=ord("z"):
            pair = str2[i:i+2]
            dic2[pair] = dic2.get(pair,0)+1
    a = set(list(dic1.keys()) + list(dic2.keys()))
    up = 0
    down = 0
    for key in a:
        up += min(dic1.get(key,0), dic2.get(key,0))
        down += max(dic1.get(key,0), dic2.get(key,0))
    print(up,down)
    if down==0:
        return 65536
    return int(up/down*65536)

