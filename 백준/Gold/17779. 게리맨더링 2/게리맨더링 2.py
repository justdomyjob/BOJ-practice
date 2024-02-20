N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

def no(y,x):
    if 0<=y <N and 0<=x <N:
        return False
    else:
        return True

all_people = 0
for i in range(N):
    for j in range(N):
        all_people+=graph[i][j]

def where(i,j,up,left,right,bottom):
    if i<left[0] and j<=up[1] and i + j <left[0]+left[1]:
        return 0
    elif i<=right[0] and j>up[1] and i - j < right[0] - right[1]:
        return 1
    elif i>=left[0] and j<bottom[1] and i - j > left[0] - left[1]:
        return 2
    elif i>right[0] and j>=bottom[1] and i + j > right[0]+right[1]:
        return 3
    else:
        return 4

minimum = 10**9
for y in range(N):
    for x in range(N):
        for d1 in range(1,N):
            for d2 in range(1,N):
                cities = [0, 0, 0, 0, 0]
                up = (y,x)
                left = (y+d1, x-d1)
                right = (y+d2, x+d2)
                bottom = (y+d1+d2,x-d1+d2)
                if no(*left) or no(*right) or no(*bottom):
                    continue
                for i in range(N):
                    for j in range(N):
                        city = where(i,j,up,left,right,bottom)
                        cities[city] += graph[i][j]
                # if y==3 and x==1 and d1==1 and d2==1:
                #     print(cities)
                difference = max(cities) - min(cities)
                minimum = min(minimum,difference)
print(minimum)