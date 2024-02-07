def solution(sizes):
    sizes.sort(key = lambda x:(-max(x[0],x[1]),-min(x[0],x[1]) ))
    MAX1 = max(sizes[0])
    a = [min(i) for i in sizes]
    MAX2 = max(a)
    
    
    return MAX1*MAX2