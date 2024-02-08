from collections import deque
def solution(prices):
    answer = [0] * len(prices)
    stack = deque()
    for time,price in enumerate(prices):
        if not stack:
            stack.append((price,time))
        if stack:
            if stack[-1][0] <= price:
                stack.append((price,time))
            else:
                while stack and stack[-1][0] > price:
                    price1, time1 = stack.pop()
                    answer[time1] = time - time1
                stack.append((price,time))
    while stack:
        price,time = stack.pop()
        answer[time] = len(prices)-1 -time
    return answer