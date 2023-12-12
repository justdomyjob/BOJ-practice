try : standard_input = open("input.txt", "r")  
except:pass

N =int(input())
k =int(input())

from bisect import bisect_left, bisect_right
def nth(a): #a가 몇번째 수인지를 리턴
    nsmall=0
    nsame=0
    for i in range(1,N+1):
        if a%i==0:
            if a <= N*i :
                nsame += 1
                nsmall += (a//i -1)
            else:  # a>N
                nsame += 0 
                nsmall += min(a//i,N)
        else:
            nsmall += min((a//i),N)
    return (nsmall, nsame)

left = 0
right = min(10**9, N*N) + 1
mid = (left+right)//2

while left + 1 < right:
    smaller = nth(mid)[0]
    same = nth(mid)[1]
    if smaller < k <=smaller +same:
        break
    elif k > smaller + same:
        left = mid
    else : 
        right =mid
    mid = (right+left)//2
print(mid)