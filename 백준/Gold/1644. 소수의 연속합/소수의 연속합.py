import math

n = int(input())

primes = []
square_root = math.floor(math.sqrt(n))

array = [True for i in range(n+1)]
for i in range(2, int(square_root)+1):
    if array[i] == True:
        j = 2
        while i*j <= n:
            array[i*j] = False
            j+=1

for i in range(2,n+1):
    if array[i]==True:
        primes.append(i)

primes_sequence_sum = [0]
temp_sum = 0
for i in range(len(primes)):
    temp_sum += primes[i]
    primes_sequence_sum.append(temp_sum)

start = 0
end = 1
length = len(primes_sequence_sum)
ret = 0
while end < length :
    if primes_sequence_sum[end] - primes_sequence_sum[start] < n:
        end+=1
    elif primes_sequence_sum[end] - primes_sequence_sum[start] > n:
        start+=1
    else:
        end +=1
        ret +=1
print(ret)
