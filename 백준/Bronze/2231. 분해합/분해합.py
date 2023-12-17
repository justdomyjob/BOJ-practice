try : standard_input = open("input.txt", "r")  
except:pass

n = int(input())
ans = 0
for i in range(n):
    number = str(i)
    sum=i
    for num in number:
        sum+=int(num)
    if sum ==n:
        ans = i
        break
print(ans)