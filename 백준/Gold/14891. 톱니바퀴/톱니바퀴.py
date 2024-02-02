from collections import deque

wheel = []
TOP, RIGHT, LEFT = 0,2,6
CLOCK, ACLOCK = 1, -1

for _ in range(4):
    q =deque()
    string = input()
    for c in string:
        q.append(int(c))
    wheel.append(q)

def right_number(q):
    return q[RIGHT]
def top_number(q):
    return q[TOP]
def left_number(q):
    return q[LEFT]

def rotate(q,dir):
    q.rotate(dir)

#함수 한번에 나중에 돌려야됨

def rotate_all(r):
    for i in range(4):
        rotate(wheel[i],r[i])

def op1(dir):
    r =[0,0,0,0]
    r[0] = dir
    if wheel[0][RIGHT]==wheel[1][LEFT]:
        pass
    elif wheel[0][RIGHT]!=wheel[1][LEFT]:
        r[1] = -dir
        if wheel[1][RIGHT] == wheel[2][LEFT]:
            pass
        elif wheel[1][RIGHT] != wheel[2][LEFT]:
            r[2] = dir
            if wheel[2][RIGHT] == wheel[3][LEFT]:
                pass
            elif wheel[2][RIGHT] != wheel[3][LEFT]:
                r[3] = -dir
    rotate_all(r)

def op4(dir):
    r = [0, 0, 0, 0]
    r[3]=dir
    if wheel[3][LEFT]==wheel[2][RIGHT]:
        pass
    elif wheel[3][LEFT]!=wheel[2][RIGHT]:
        r[2]= -dir
        if wheel[2][LEFT] == wheel[1][RIGHT]:
            pass
        elif wheel[2][LEFT] != wheel[1][RIGHT]:
            r[1] = dir
            if wheel[1][LEFT] == wheel[0][RIGHT]:
                pass
            elif wheel[1][LEFT] != wheel[0][RIGHT]:
                r[0] = -dir
    rotate_all(r)
def op2(dir):
    r = [0, 0, 0, 0]
    r[1] = dir
    if wheel[1][LEFT]==wheel[0][RIGHT]:
        pass
    elif wheel[1][LEFT]!=wheel[0][RIGHT]:
        r[0] = -dir
    if wheel[1][RIGHT] == wheel[2][LEFT]:
        pass
    elif wheel[1][RIGHT] != wheel[2][LEFT]:
        r[2] = -dir
        if wheel[2][RIGHT] == wheel[3][LEFT]:
            pass
        elif wheel[2][RIGHT] != wheel[3][LEFT]:
            r[3] = dir
    rotate_all(r)
def op3(dir):
    r = [0, 0, 0, 0]
    r[2] = dir
    if wheel[2][RIGHT]==wheel[3][LEFT]:
        pass
    elif wheel[2][RIGHT]!=wheel[3][LEFT]:
        r[3] = -dir
    if wheel[1][RIGHT] == wheel[2][LEFT]:
        pass
    elif wheel[1][RIGHT] != wheel[2][LEFT]:
        r[1] = -dir
        if wheel[0][RIGHT] == wheel[1][LEFT]:
            pass
        elif wheel[0][RIGHT] != wheel[1][LEFT]:
            r[0] = dir
    rotate_all(r)

op = int(input())
ops = [None,op1,op2,op3,op4]
for _ in range(op):
    num, dir = map(int,input().split())
    ops[num](dir)

s = 0
for i in range(4):
    s += (wheel[i][TOP] * (2**i))
print(s)
