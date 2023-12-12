try : standard_input = open("input.txt", "r")  
except:pass

home_n, wifi = map(int,input().split())
home_list = [int(input()) for _ in range(home_n)]
home_list.sort()

def can_install(length):
    install_house_n = 1 #설치한 집 개수 (0번째 집은 미리 설치)
    before_install_house =0 # 이전에 설치한 집
    now = 1 #현재 집 
    #now_x =0 #현재 x좌표
    while now <= home_n-1 and install_house_n < wifi :
        if home_list[now] - home_list[before_install_house] >= length:
            before_install_house = now
            now = now+1
            install_house_n +=1
        else :
            now = now +1
    if install_house_n ==wifi:
        return True
    else:
        return False

left = 1
#right = max(home_list)-min(home_list) +1 #을 하는 이유? 알아보자 right가 답이 될때가 있어서
right = (max(home_list)-min(home_list))//(wifi-1) +1
mid = (left+right)//2
while left +1 < right:
    if can_install(mid):
        left = mid
    else :
        right = mid
    mid = (left+right)//2 
print(mid)
