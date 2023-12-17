try : standard_input = open("input.txt", "r")  
except:pass

dp={}
def recur(a,b,c):
    if (a,b,c) in dp:
        return dp[(a,b,c)]
    elif a <= 0 or b <= 0 or c <= 0:
        dp[(a,b,c)]=1
        return 1
    elif a > 20 or b > 20 or c > 20 :
        dp[(a,b,c)] = recur(20,20,20)
        return dp[(a,b,c)]

    elif a < b and b < c:
        dp[(a,b,c)] = recur(a,b,c-1) + recur(a,b-1,c-1) - recur(a,b-1,c)
        return dp[(a,b,c)]

    else:
        dp[(a,b,c)] = recur(a-1, b, c) + recur(a-1, b-1, c) + recur(a-1, b, c-1) - recur(a-1, b-1, c-1)
        return  dp[(a,b,c)]
    
while True:
    a,b,c = map(int,input().split())
    if a==-1 and b==-1 and c==-1 :
        break
    print(f"w({a}, {b}, {c}) = {recur(a,b,c)}")

