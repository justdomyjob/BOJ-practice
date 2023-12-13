try : standard_input = open("input.txt", "r")  
except:pass

n = int(input())
color = [] #하얀색 0, 파란색1
for _ in range(n):
    color.append(list(map(int,input().split())))

def get_white_blue(n,color):
    if n==1:
        if color[0][0] == 0:
            return (1,0)
        else:
            return (0,1)
    else:
        left_top = [color[i][:n//2] for i in range(n//2)]
        right_top = [color[i][n//2:] for i in range(n//2)]
        left_bottom = [color[i][:n//2] for i in range(n//2,n)]
        right_bottom = [color[i][n//2:] for i in range(n//2,n)]
        lt = get_white_blue(n//2, left_top)
        rt = get_white_blue(n//2, right_top)
        lb = get_white_blue(n//2, left_bottom)
        rb = get_white_blue(n//2, right_bottom)
        if lt==rt==lb==rb==(1,0):
            return (1,0)
        elif lt==rt==lb==rb==(0,1):
            return (0,1)
        else:
            return (lt[0]+rt[0]+lb[0]+rb[0], lt[1]+rt[1]+lb[1]+rb[1])  
(a,b) = get_white_blue(n,color)
print(a,b, sep="\n")
