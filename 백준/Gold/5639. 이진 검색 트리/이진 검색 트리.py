import sys
sys.setrecursionlimit(10**4)
a = sys.stdin.readlines()
node_list = [int(i) for i in a]

def post(trees):
    if len(trees)==0:
        return
    
    root = trees[0]
    left_tree = [i for i in trees[1:] if i < root]
    right_tree = [i for i in trees[1:] if i > root]

    post(left_tree)
    post(right_tree)
    print(root)

post(node_list)