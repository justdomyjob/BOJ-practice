def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        num = arr1[i] |  arr2[i]
        answer.append(num)
    ret = []
    for i in range(n):
        temp = ""
        for j in range(n-1,-1,-1):
            if answer[i] & 2**j:
                temp+="#"
            else:
                temp+=" "
        ret.append(temp)
    print(ret)
    return ret