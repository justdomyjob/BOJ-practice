try : standard_input = open("input.txt", "r")  
except:pass

n = input()
i = 0
j = 1

def six(n):
    if "666" in n:
        return True
    
while i!=int(n):
    j+=1
    if six(str(j)):
        i+=1
print(j)