def solution(sizes):
    a = [max(i) for i in sizes]
    MAX1 = max(a)
    b = [min(i) for i in sizes]
    MAX2 = max(b)
    
    
    return MAX1*MAX2