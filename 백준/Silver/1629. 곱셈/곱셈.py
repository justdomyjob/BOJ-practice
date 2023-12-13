try : standard_input = open("input.txt", "r")  
except:pass

a,b,c = map(int,input().split())

def remain(a,b,c):
    if b==1:
        return a%c
    else:
        if b%2==0:
            ret = (remain(a,b//2,c)**2)%c
            return ret
        else:
            ret = (remain(a,b//2,c)**2)*a
            ret= ret%c
            return ret
print(remain(a,b,c))           