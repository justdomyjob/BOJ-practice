numbers = ["0","1","2","3","4","5","6","7","8","9"] 
def solution(dartResult):
    ret = 0
    shots = []
    scores = []
    a= []
    for i in range(2,len(dartResult)):
        if dartResult[i] in numbers and dartResult[i-1] not in numbers:
            a.append(i)
    shots.append(dartResult[:a[0]])
    shots.append(dartResult[a[0]:a[1]])
    shots.append(dartResult[a[1]:])
    
    for shot in shots:
        for i in range(len(shot)):
            if shot[i] not in numbers:
                scores.append(int(shot[:i]))
                break
    print(scores)
    
    for i in range(3):
        shot = shots[i]
        for j in range(len(shot)):
            if shot[j] not in numbers:
                if shot[j] == "D":
                    scores[i] = scores[i] **2
                elif shot[j] == "T":
                    scores[i] = scores[i] **3
                elif shot[j] == "*":
                    if i ==0:
                        scores[i] *=2
                    else:
                        scores[i] *=2
                        scores[i-1] *=2
                elif shot[j] == "#":
                    scores[i] *=-1
    print(scores)
    return sum(scores)
