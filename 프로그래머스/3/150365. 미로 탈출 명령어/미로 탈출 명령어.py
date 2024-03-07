
dy = [-1,0,1,0]
dx = [0,1,0,-1]

#abc d efghijk l mnopq r st u vwxz
# 아래 왼 오 위
def solution(n, m, x, y, r, c, k):
    def distance(x,y,r,c):
        return abs(x-r) + abs(y-c)

    answer = ''
    d = distance(x, y, r, c)
    if (d%2) != (k%2):
        return "impossible"
    elif d > k :
        return "impossible"
    while k:
        if k == distance(x, y, r, c):
            if x<r and y >=c:
                answer+= "d" *abs(x-r) + "l" * abs(y-c)
                break
            elif x>=r and y >=c:
                answer += "l" * abs(y-c) + "u" *abs(x-r)
                break
            elif x>=r and y <c:
                answer +=  "r" * abs(y-c) + "u" *abs(x-r)
                break
            else:
                answer += "d" * abs(x-r) + "r" * abs(y-c)
                break
        else:
            if x+1 <=n :
                x+=1
                answer+="d"
            elif y-1 >=1:
                answer += "l"
                y-=1
            else:
                answer += "r"
                y+=1
            k-=1
    print(answer)
    return answer

solution(	3, 4, 2, 3, 3, 1, 5)