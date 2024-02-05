n = int(input())

def find(n):
    for i in range(10000):
        if (i-1)*i/2 < n <= i*(i+1)/2:
            break
    return i

k = find(n)
if k%2==0:
    b = k - (n-1 - (k-1)*k//2)
    a = (n- (k-1)*k//2)
    print(a, end = "")
    print("/", end = "")
    print(b)
else:
    a = k - (n - 1 - (k - 1) * k // 2)
    b = (n - (k - 1) * k // 2)
    print(a, end="")
    print("/", end="")
    print(b)