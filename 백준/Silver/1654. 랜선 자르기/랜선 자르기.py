try : standard_input = open("input.txt", "r")  
except:pass

k, n = map(int,input().split())
k_list = []
for _ in range(k):
    k_list.append(int(input()))

k_list.sort()
def get_ransun(length):
    sum = 0
    for k in k_list:
        sum += k//length
    return sum

length = max(k_list)
left = 1
right = max(k_list)
while right-left>1:
    if get_ransun(length) < n:
         right = length
         length = (left+right)//2
    else : 
        left = length
        length = (left+right)//2
print(length)

        