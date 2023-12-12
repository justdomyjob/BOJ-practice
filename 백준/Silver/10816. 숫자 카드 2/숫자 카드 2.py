try : standard_input = open("input.txt", "r")  
except:pass

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

from bisect import bisect_left, bisect_right

def binary_count(a):
    return bisect_right(n_list,a) - bisect_left(n_list,a)

for element in m_list[:-1]:
    print(binary_count(element), end=" ")
print(binary_count(m_list[-1]))

