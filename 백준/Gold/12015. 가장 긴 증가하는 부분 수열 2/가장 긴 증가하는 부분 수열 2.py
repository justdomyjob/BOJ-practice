try : standard_input = open("input.txt", "r")  
except:pass

n = int(input())
sequence = list(map(int,input().split()))

LIS = []
LIS.append(sequence[0])

from bisect import bisect_left, bisect_right
for A in sequence[1:]:
    if A > LIS[-1]:
        LIS.append(A)
    else:
        index = bisect_left(LIS,A)
        LIS[index] = A #바꾸기
print(len(LIS))
            