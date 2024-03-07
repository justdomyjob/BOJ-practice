def solution(numbers):
    answer = []
    for n in numbers:
        a = bin(n)[2:]
        result = check(a)
        answer.append(result)
    print(answer)
    return answer

def check(a):
    if a == "1":
        return 1
    i = 0
    length = len(a)
    while not (2**i-1 < length <= 2**(i+1)-1) :
        i+=1
    left =a[:length - 2**i].zfill(2**i-1)
    mid = a[length - 2**i]
    right = a[length - 2**i +1 : ]
    if mid == "0":
        if "1" in left or "1" in right:
            return 0
        else:
            return 1
    else:
        if check(left) and check(right):
            return 1
        else:
            return 0

solution([7,42,5,63,11,95])


#1 000 가능 => 없 1 000

#왼쪽 |중간| 오른쪽 나누는데
#만약 중간이 0이면 왼쪽 오른쪽은 모두 0이어야 됨
#만약 중간이 1이면 왼쪽 오른쪽은 이진트리거나 모두 0이면 됨
#2 i승 -1 < length <= 2 i+1 승 -1인 i를 찾아야됨