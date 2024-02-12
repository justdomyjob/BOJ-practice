def solution(price, money, count):
    require = count*(count+1)//2 * price
    if require <= money:
        return 0
    else:
        return require - money
