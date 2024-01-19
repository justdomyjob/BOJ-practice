def solution(s):
    s = s.split(" ")
    s = [int(i) for i in s]
    a = min(s)
    b = max(s)
    answer = str(a) + " " + str(b)
    return answer
