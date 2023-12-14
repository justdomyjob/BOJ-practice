try : standard_input = open("input.txt", "r")  
except:pass

n = int(input())
distance = list(map(int,input().split()))
liter_price = list(map(int,input().split()))

i=0
current_place = 0
sum = 0
while i < len(distance):
    if liter_price[current_place] <= liter_price[i]:
        sum += liter_price[current_place] * distance[i]
    else:
        current_place = i
        sum += liter_price[current_place] * distance[i]
    i+=1
print(sum)