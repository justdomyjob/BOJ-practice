
def solution(n, tops):
    #a[k] = a[k-1] + b[k-1]
    #b[k] = 1번: 있으면 a[k-1]+b[k-1]
        #   2번 : b[k-1]
        #   4번 : a[k=1]+b[k-1]

    if tops[0] ==1:
        a = [0, 1]
        b = [0, 3]
    else:
        a = [0, 1]
        b = [0, 2]
    for i in tops[1:]:
        A = a[-1]
        B = b[-1]
        if i == 1:
            a.append((A+B)%10007)
            b.append((2 * A+ 3 * B)%10007)
        else:
            a.append((A + B)%10007)
            b.append((A + 2 * B)%10007)

    return (a[-1]+b[-1])%10007