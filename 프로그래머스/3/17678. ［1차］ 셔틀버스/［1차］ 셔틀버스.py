def solution(n, t, m, timetable):
    ret = 0
    dic = {}
    for i in range(n):
        dic[540+i*t] = []
    timetable = [change(time) for time in timetable]
    timetable.sort()
    for time in timetable:
        for i in range(n):
            if time <= 540+i*t and len(dic[540+i*t]) < m:
                dic[540+i*t].append(time)
                break
    if len(dic[540+(n-1)*t]) == m:
        ret = dic[540+(n-1)*t][-1]-1
    else:
        ret = 540+(n-1)*t
    hour = str(ret//60).rjust(2,"0")
    minute = str(ret%60).rjust(2,"0")
    return hour+":"+minute

def change(time):
    t = time.split(":")
    return 60*int(t[0]) + int(t[1])
def can(n,t,m,timetable, time):
    return True
