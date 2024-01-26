import sys

input = sys.stdin.readline
n,m,r,c,k = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
ops = list(map(int,input().split()))

steps={1:(0,1),2:(0,-1),3:(-1,0),4:(1,0)} #동서북남 순서

class Dice:
    def __init__(self,up,bottom,north,south,east,west):
        self.up = up
        self.bottom = bottom
        self.north = north
        self.south = south
        self.east = east
        self.west = west
    def __str__(self):
        return (f"up :{self.up} bottom :{self.bottom} north :{self.north} "
              f"south :{self.south} east :{self.east} west :{self.west} ")

def dice_east(dice):
    temp = dice.west
    dice.west = dice.bottom
    dice.bottom = dice.east
    dice.east = dice.up
    dice.up = temp
def dice_west(dice):
    temp = dice.east
    dice.east = dice.bottom
    dice.bottom = dice.west
    dice.west = dice.up
    dice.up = temp
def dice_north(dice):
    temp = dice.up
    dice.up = dice.south
    dice.south = dice.bottom
    dice.bottom = dice.north
    dice.north = temp
def dice_south(dice):
    temp = dice.up
    dice.up = dice.north
    dice.north = dice.bottom
    dice.bottom = dice.south
    dice.south = temp
dice_step = {1:dice_east,2:dice_west,3:dice_north,4:dice_south}

def swap_number(dice):
    global r,c
    if graph[r][c]==0:
        graph[r][c] = dice.bottom
    else:
        dice.bottom = graph[r][c]
        graph[r][c] = 0

dice = Dice(0,0,0,0,0,0)
for op in ops:
    step = steps[op]
    new_r = r+step[0]
    new_c = c+step[1]
    if 0<=new_r<n and 0<=new_c<m:
        r = new_r
        c = new_c
        dice_step[op](dice)
        swap_number(dice)
        print(dice.up)
    else:
        continue