import copy
from collections import deque

numbers = deque(list(map(int,input().split())))
board = [0 for _ in range(101)]
board[1:20] = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40]
board[30:34] = [10,13,16,19,25]
board[50:53] = [20,22,24,25]
board[70:74] = [30,28,27,26,25]
board[80:83] = [25,30,35,40]
board[90] = 40
horses = [0,0,0,0]
dic = {}
dic2 = {}
dic2[5] = 30
dic2[10] = 50
dic2[15] = 70

dic[20] = 90
dic[34] =  80
dic[53] = 80
dic[74] = 80
dic[83] = 90

max_score = 0

def finish(place):
    if place>90:
        return True
    else:
        return False

def duplicate(after,horses):
    if after in horses:
        return True
    if board[after] in [board[horse] for horse in horses]:
        return True
    else :
        return False
def move(horses, h, move):
    after = horses[h]
    for _ in range(move):
        after += 1
        if after in dic:
            after = dic[after]
    if after in dic2:
        after = dic2[after]
    horses[h] = after
    return board[after]


def can_move(horses, h, move):
    current = horses[h]
    if finish(current):
        return False
    after = current
    for _ in range(move):
        after+=1
        if after in dic:
            after = dic[after]
    if after in dic2:
        after = dic2[after]
    if finish(after):
        return True
    if after in horses:
        return False
    else:
        return True


def dfs(numbers,horses,n,scores):
    global max_score
    if n == 10:
        max_score = max(max_score,scores)
        return
    number = numbers.popleft()
    for h in range(4):
        if can_move(horses,h,number):
            temp_numbers = copy.deepcopy(numbers)
            temp_horses = copy.deepcopy(horses)
            score = move(temp_horses,h,number)
            dfs(temp_numbers,temp_horses,n+1,scores+score)
    numbers.appendleft(number)
dfs(numbers,horses,0,0)
print(max_score)
