dic = {}
count = 0
while True:
    try:
        a = input()
    except:
        break
    dic[a] = dic.get(a,0)+1
    count+=1
keys = list(dic.keys())
keys.sort()
for key in keys:
    print(f"{key} {dic[key]/count*100:.4f}")