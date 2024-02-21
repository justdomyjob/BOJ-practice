from collections import deque

N,K = map(int,input().split())
q = deque(list(map(int,input().split())))
robot = deque([0 for _ in range(N)])
stage = 0
while q.count(0) < K:
    q.rotate(1)
    robot.rotate(1)
    robot[0] = 0
    robot[N-1] = 0
    for i in range(N-2,-1,-1):
        if robot[i] ==1 and not (robot[i+1]==1 or q[i+1]==0):
            robot[i+1] =1
            robot[i] = 0
            q[i+1]-=1
    robot[N-1] = 0
    if q[0] >0:
        robot[0] = 1
        q[0]-=1
    stage+=1
print(stage)