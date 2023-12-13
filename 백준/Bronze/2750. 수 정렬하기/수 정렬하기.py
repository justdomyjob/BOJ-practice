try : standard_input = open("input.txt", "r")  
except:pass

n = int(input())
l = [int(input()) for _ in range(n)]
l.sort()
for ll in l:
    print(ll)