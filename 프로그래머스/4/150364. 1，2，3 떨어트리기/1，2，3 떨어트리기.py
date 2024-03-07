from collections import defaultdict, deque


def solution(edges, target):
    child = defaultdict(list)
    order = [[] for _ in range(len(target))]
    for a,b in edges:
        child[a].append(b)
    for key in child:
        child[key].sort()
        child[key] = deque(child[key])
    i=1
    while True:
        start = 1
        while True:
            if start in child:
                next = child[start][0]
                child[start].rotate(-1)
                start = next
            else:
                order[start-1].append(i)
                break
        check = []
        for j in range(len(target)):
            length = len(order[j])
            number = target[j]
            if number < length:
                check.append(1)
            elif length <= number <= 3*length:
                check.append(2)
            else:
                check.append(3)
        if 1 in check:
            return [-1]
        elif 3 not in check:
            break
        else:
            i+=1
            continue
    answer = [0 for _ in range(i)]
    for k in range(len(target)):
        if target[k] > 0:
            length = len(order[k])
            for o in order[k]:
                if 1 + 3 * (length - 1) >= target[k]:
                    answer[o-1] = 1
                    target[k]-=1
                elif 2 + 3 * (length - 1) >= target[k]:
                    answer[o - 1] = 2
                    target[k]-=2
                else :
                    answer[o - 1] = 3
                    target[k]-=3
                length-=1
    return answer


print(solution([[2, 4], [1, 2], [6, 8], [1, 3], [5, 7], [2, 5], [3, 6], [6, 10], [6, 9]],[0, 0, 0, 3, 0, 0, 5, 1, 2, 3]))
# print(solution([[1, 3], [1, 2]],	[0, 7, 1]))