try :
    standard_input = open("input.txt", "r")
except:
    pass

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

def include(a,left,right):
    if a < n_list[left] or a > n_list[right] :
        return 0
    if a == n_list[left] or a== n_list[right]:
        return 1
    else:
        middle = (left+right)//2
        if a  <= n_list[middle]:
            return include(a, left, middle)
        else :
            return include(a, middle+1, right)

for element in m_list:
    print(include(element,0,n-1))


