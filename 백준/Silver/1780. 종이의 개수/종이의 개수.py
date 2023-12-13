try : standard_input = open("input.txt", "r")  
except:pass
import sys
n = int(sys.stdin.readline().rstrip())
color = []
for _ in range(n):
    color.append(list(map(int,sys.stdin.readline().rstrip().split())))
    

def get_white_blue(n,x,y):
    if n==1:
        if color[x][y] == -1:
            return [1,0,0]
        elif color[x][y] == 0:
            return [0,1,0]
        else:
            return [0,0,1]
    else:
        temp = [0,0,0]
        for i in range(3):
            for j in range(3):
                divided = get_white_blue(n//3, x+i*n//3, y+j*n//3)
                for k in range(3):
                    temp[k] += divided[k]
        if temp == [9,0,0]:
            temp = [1,0,0]
        elif temp == [0,9,0]:
            temp = [0,1,0]    
        elif temp == [0,0,9]:
            temp = [0,0,1]
        return temp
temp = get_white_blue(n,0,0)
for t in temp:
    print(t)