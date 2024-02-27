from collections import deque


def solution(stones, k):
    q = deque() #index, 높이
    array =[0 for _ in range(len(stones))]
    for i,stone in enumerate(stones):
        while q and q[-1][1] < stone:
            (index, height) = q.pop()
            array[index] = (height,i-index)
        q.append((i,stone))
    while q:
        (index,height) = q.pop()
        array[index] = (height, len(stones) - index)

    q2 = deque()  # index, 높이
    array2 = [0 for _ in range(len(stones))]
    for i,stone in enumerate(stones[::-1]):
        while q2 and q2[-1][1] < stone:
            (index, height) = q2.pop()
            array2[index] = (height,i-index)
        q2.append((i,stone))

    while q2:
        (index,height) = q2.pop()
        array2[index] = (height, len(stones) - index)
    array2 = array2[::-1]

    array3 = [(a[0],a[1]+b[1]-1) for a,b in zip(array,array2)]
    minimum = 10**9
    for height,length in array3:
        if length>=k:
            minimum = min(minimum,height)


    return minimum

# solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3)