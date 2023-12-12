try : standard_input = open("input.txt", "r")  
except:pass

tree_n , tree_meter = map(int,input().split())
tree_list = list(map(int,input().split()))

left = 0
right = max(tree_list)
mid = (left+right)//2

def get_tree(a):
    sum = 0
    for tree in tree_list:
        if tree>= a:
            sum+=(tree-a)
    return sum
while left+1 < right:
    if get_tree(mid) < tree_meter:
        right = mid
    else:
        left = mid
    mid = (left+right)//2
print(mid)
