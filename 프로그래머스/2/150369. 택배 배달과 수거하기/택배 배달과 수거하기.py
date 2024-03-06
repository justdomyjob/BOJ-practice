def solution(cap, n, deliveries, pickups):
    delivery = []
    pickup = []
    for i,v in enumerate(deliveries):
        if v!= 0 :
            delivery.append([i+1,v])
    for i,v in enumerate(pickups):
        if v!= 0 :
            pickup.append([i+1,v])

    ret = 0
    while delivery and pickup:
        cap1 = cap
        cap2 = cap
        distance = max(delivery[-1][0], pickup[-1][0])
        while cap1 > 0 and delivery:
            if cap1 >= delivery[-1][1]:
                cap1 -= delivery[-1][1]
                delivery.pop()
            else:
                delivery[-1][1] -= cap1
                cap1 = 0
        while cap2 > 0 and pickup:
            if cap2 >= pickup[-1][1]:
                cap2 -= pickup[-1][1]
                pickup.pop()
            else:
                pickup[-1][1] -= cap2
                cap2 = 0
        ret+= 2 * distance
    while delivery:
        cap1 = cap
        distance = delivery[-1][0]
        while cap1 > 0 and delivery:
            if cap1 >= delivery[-1][1]:
                cap1 -= delivery[-1][1]
                delivery.pop()
            else:
                delivery[-1][1] -= cap1
                cap1 = 0
        ret += 2 * distance
    while pickup:
        cap2 = cap
        distance = pickup[-1][0]
        while cap2 > 0 and pickup:
            if cap2 >= pickup[-1][1]:
                cap2 -= pickup[-1][1]
                pickup.pop()
            else:
                pickup[-1][1] -= cap2
                cap2 = 0
        ret+= 2 * distance
    print(ret)
    return ret

