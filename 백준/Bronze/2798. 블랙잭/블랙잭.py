try : standard_input = open("input.txt", "r")  
except:pass

from itertools import combinations

n, m = map(int,input().split())
num_list = list(map(int,input().split()))

result = list(combinations(num_list,3))
max = 0
for element in result:
    sum3 = sum(element)
    if sum3<= m and sum3>max:
        max = sum3
print(max)