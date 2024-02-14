import sys
sys.setrecursionlimit(10**6)
def solution(nodeinfo):
    tree = {}
    nodes = []
    for i,(x,y) in enumerate(nodeinfo):
        tree[i+1] = Node((x,y),None,None)
        nodes.append((x,y,i+1))
    nodes.sort(key = lambda x: (-x[1],x[0]))

    def find_child(i1,childs):
        my_node = tree[i1]
        x1,y1 = tree[i1].data
        if not childs:
            return
        left_childs = sorted([(x, y, i) for x, y, i in childs if x < x1], key = lambda x:-x[1])
        right_childs = sorted([(x, y, i) for x, y, i in childs if x > x1],key = lambda x:-x[1])
        if left_childs:
            left_child = left_childs[0][2]
            my_node.left = left_child
            find_child(left_child,left_childs[1:])
        if right_childs:
            right_child = right_childs[0][2]
            my_node.right = right_child
            find_child(right_child, right_childs[1:])
    def pre_order(i):
        my_node = tree[i]
        ret = [i]
        if my_node.left:
            ret.extend(pre_order(my_node.left))
        if my_node.right:
            ret.extend(pre_order(my_node.right))
        return ret
    def post_order(i):
        my_node = tree[i]
        ret = []
        if my_node.left:
            ret.extend(post_order(my_node.left))
        if my_node.right:
            ret.extend(post_order(my_node.right))
        ret.append(i)
        return ret
    find_child(nodes[0][2],nodes[1:])
    ret = [pre_order(nodes[0][2]),post_order(nodes[0][2])]
    return ret

class Node:
    def __init__(self, data,left,right):
        self.data = data
        self.left = left
        self.right = right

assert solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]) == [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
assert solution([[5,3]]) == [[1],[1]]