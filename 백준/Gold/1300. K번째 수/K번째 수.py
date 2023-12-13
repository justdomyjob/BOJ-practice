try : standard_input = open("input.txt", "r")  
except:pass

N =int(input())
k =int(input())

from bisect import bisect_left, bisect_right
def nsmall(a): #ㄴㅇㄻㄴㄷㅇㄻ니아ㅓㅣ
    smaller=0
    for i in range(1,N+1):
        smaller += min((a//i),N)
    return smaller

left = 0
right = min(10**9, N*N)
mid = (left+right)//2

while left +1 < right:
    smaller = nsmall(mid)
    if k > smaller: #mid는 더 커져야됨
        left = mid
    else : 
        right =mid
    mid = (right+left)//2
print(mid+1) 