def solution(today, terms, privacies):
    DAY = 28
    MONTH = 12
    y,m,d = today.split(".")
    y = int(y)
    m = int(m)
    d = int(d)
    today_count = y*MONTH*DAY+m*DAY+d
    dic = {}
    for term in terms:
        alpha,month = term.split()
        day = int(month) * DAY
        dic[alpha] = day
    answer = []
    for i,pri in enumerate(privacies):
        number = i+1
        day,alpha = pri.split()
        y,m,d = day.split(".")
        y = int(y)
        m = int(m)
        d = int(d)
        before_day = y*MONTH*DAY+m*DAY+d
        if today_count - before_day <= dic[alpha] -1 :
            continue
        else:
             answer.append(number)

    return answer

