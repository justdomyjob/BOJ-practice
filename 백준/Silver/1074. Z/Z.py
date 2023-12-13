try : standard_input = open("input.txt", "r")  
except:pass

N, r, c = map(int,input().split())
n = 2**N
def order(n, r,c):
    if n==1:
        return 0
    else:
        if r < n//2 and c < n//2:
            return order(n//2, r, c) 
        elif r <n //2 and c >= n//2:
            return (n//2)**2 + order(n//2, r,c -n//2)
        elif r >=n //2 and c < n//2:
            return (n//2)**2*2 + order(n//2, r-n//2, c)
        else:
            return (n//2)**2*3 + order(n//2, r-n//2, c-n//2 )
print(order(n,r,c))