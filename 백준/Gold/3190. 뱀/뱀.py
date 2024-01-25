import sys

input = sys.stdin.readline
n =int(input())
NONE = 0
APPLE = 1
ME = 2
graph = [[NONE for _ in range(n)] for _ in range(n)]
tail_direction = [[0 for _ in range(n)] for _ in range(n)]
apple_n = int(input())

for _ in range(apple_n):
    a,b = map(int,input().split())
    graph[a-1][b-1] = APPLE

directions = {}
for _ in range(int(input())):
    sec, direction = input().split()
    sec = int(sec)
    directions[sec]=direction

def game_over():
    global r, c
    if r < 0 or r >= n or c < 0 or c >= n:
        return True
    if graph[r][c] == ME:
        return True
    return False


def go():
    global r, c, d
    tail_direction[r][c]=d
    if d == 0:
        r = r - 1
    elif d == 1:
        c = c + 1
    elif d == 2:
        r = r + 1
    elif d == 3:
        c = c - 1

def go_tail():
    global tail_r, tail_c, tail_d
    tail_d =  tail_direction[tail_r][tail_c]
    if tail_d == 0:
        tail_r = tail_r - 1
    elif tail_d == 1:
        tail_c = tail_c + 1
    elif tail_d == 2:
        tail_r = tail_r + 1
    elif tail_d == 3:
        tail_c = tail_c - 1

def remove_tail():
    global tail_r,tail_c
    graph[tail_r][tail_c] = NONE
    go_tail()

def mark_myself():  # 사과 먹고 내 위치 표시
    global r,c
    global tail_r,tail_c
    if graph[r][c]!=APPLE:
        remove_tail()
    graph[r][c] = ME

def change_direction():
    global count
    global d
    direction = directions.get(count,"no")
    if direction=="no":
        return
    elif direction =="D":
        d=(d+1)%4
    elif direction == "L":
        d = (d -1) % 4
    else:
        print("error")

r, c, d = 0, 0, 1
tail_r, tail_c, tail_d = 0, 0, 1
count = 0

while True:
    change_direction()
    go()
    count += 1
    if game_over():
        break
    mark_myself()
print(count)