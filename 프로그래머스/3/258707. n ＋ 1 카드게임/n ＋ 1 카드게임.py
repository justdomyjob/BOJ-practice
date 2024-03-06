def solution(coin, cards):
    n = len(cards)
    couple = []

    round = 1
    i = n//3
    pick = set(cards[:i])
    have = set()

    def check1():
        for i in pick:
            for j in pick:
                if i+j == n+1:
                    pick.remove(i)
                    pick.remove(j)
                    return True
        return False

    def check2():
        nonlocal coin
        if coin ==0 :
            return False
        for i in pick:
            for j in have:
                if i+j == n+1:
                    pick.remove(i)
                    have.remove(j)
                    coin-=1
                    return True
        return False

    def check3():
        nonlocal coin
        if coin <=1 :
            return False
        for i in have:
            for j in have:
                if i+j == n+1:
                    have.remove(i)
                    have.remove(j)
                    coin-=2
                    return True
        return False

    while i < n :
        n1 = cards[i]
        n2 = cards[i+1]
        have.add(n1)
        have.add(n2)
        if check1():
            pass
        elif check2():
            pass
        elif check3():
            pass
        else:
            break
        i+=2
        round+=1

    return round

# solution(4,[3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4])