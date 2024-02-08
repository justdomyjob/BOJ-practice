import math
from itertools import permutations
def solution(numbers):
    
    numbers= list(numbers)
    a = set()
    for i in range(1,len(numbers)+1):
        i_num = permutations(numbers,i)
        for num in i_num:           
            num = int("".join(num))
            if is_prime(num):
                a.add(num)
    return len(a)

def is_prime(number):
    if number==0 or number==1:
        return False
    for i in range(2,int(math.sqrt(number))+1):
        if number%i == 0:
            return False
    return True

