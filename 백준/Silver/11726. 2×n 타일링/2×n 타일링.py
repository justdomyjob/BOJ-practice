n = int(input())

dic= {1:1,2:2}

def rec(n):
    if n not in dic:
        dic[n]= rec(n-1) + rec(n-2)
    return dic[n]
print(rec(n)%10007)