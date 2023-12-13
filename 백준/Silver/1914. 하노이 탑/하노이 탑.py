try : standard_input = open("input.txt", "r")  
except:pass

n = int(input())

def hanoi_20(n,a,b): #a=>b, c는 나머지
    c = 6-a-b
    if n==1:
        print(f"{a} {b}")
    else:
        hanoi_20(n-1,a,c)
        print(f"{a} {b}")
        hanoi_20(n-1,c,b)
    return
if n<=20:
    print(2**n-1)
    hanoi_20(n,1,3)
else:
    print(2**n-1)