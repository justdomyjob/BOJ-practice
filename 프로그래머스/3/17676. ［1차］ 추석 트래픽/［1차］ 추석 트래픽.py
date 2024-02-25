def solution(lines):
    all = []
    for line in lines:
        interval = change_seconds(line)
        all.append(interval)
    all.sort(key = lambda x:(x[1],x[0]))
    dic = {}
    MAX = 0
    for start,end in all:
        for i in range(start-999, end+1):
            dic[i] = dic.get(i,0)+1
    for key in dic:
        value = dic[key]
        MAX = max(value,MAX)
    return MAX

def change_seconds(line):
    splited = line.split(" ")
    time = splited[1]
    elapsed = splited[2]
    time = time.split(":")
    end_miliseconds = int(time[0])* 3600000 + int(time[1]) * 60000
    seconds = time[2].split(".")
    end_miliseconds += int(seconds[0]) * 1000 + int(seconds[1])
    elapsed = elapsed[:-1]
    if "." in elapsed:
        time = elapsed.split(".")
        elapsed_miliseconds = int(time[0]) * 1000 + int(time[1])
    else:
        elapsed_miliseconds = int(elapsed) * 1000
    start_miliseconds = end_miliseconds - elapsed_miliseconds + 1
    return (start_miliseconds, end_miliseconds)
    