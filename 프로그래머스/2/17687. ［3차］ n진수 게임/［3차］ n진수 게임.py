def solution(n, t, m, p):
    answer = ""
    i = 0
    seq =1
    cur_t = 0
    while True:
        gin = change(i,n)
        for char in gin:
            if seq%m == p%m:
                answer+=char
                cur_t+=1
                if cur_t==t:
                    break
            seq+=1
        if cur_t==t:
            break
        i+=1
    return answer

def change(a,n): #10진법 숫자 a를 n진수로
    ret = ""
    i = 0
    if a==0:
        return "0"
    while n**i<= a :
        i+=1
    i-=1
    for j in range(i,-1,-1):
        num = str(a//(n**j))
        if num == "10":
            num = "A"
        elif num == "11":
            num = "B"
        elif num == "12":
            num = "C"
        elif num == "13":
            num = "D"
        elif num == "14":
            num = "E"
        elif num == "15":
            num = "F"
        a = a % (n**j)
        ret +=num
    return ret
        