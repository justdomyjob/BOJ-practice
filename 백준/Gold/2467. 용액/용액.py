n = int(input())
solutions = list(map(int,input().split()))
solutions.sort()

if solutions[0] > 0:
    print(solutions[0], solutions[1])
elif solutions[-1] < 0:
    print(solutions[-2], solutions[-1])
else:
    ret0, ret1 = 0,0
    low = 0
    high = len(solutions)-1
    MIN = 10**10
    while low < high:
        s = solutions[low] + solutions[high]
        if abs(s) <MIN:
            MIN = abs(s)
            ret0 = solutions[low]
            ret1 = solutions[high]
        if s > 0 :
            high -= 1
        elif s <0 :
            low += 1
        else:
            print(solutions[low], solutions[high])
            exit(0)
    print(ret0,ret1)

