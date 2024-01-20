import sys

test = int(input())
for _ in range(test):
    sig = sys.stdin.readline().rstrip()
    length =len(sig)
    flag = True

    i = 0
    while i < length:
        if sig[i]=="0" and i+1 < length:
            if sig[i+1] != "1":
                flag = False
                break
            else:
                i+=2
        elif sig[i]=="0" and i+1 >= length:
            flag = False
            break
        elif sig[i]=="1":
            num0 = 0
            i+=1
            while i < length and sig[i]=="0":
                num0+=1
                i+=1
            if num0 <2 :
                flag=False
                break
            num1 = 0
            while i < length and sig[i]=="1":
                num1+=1
                i+=1
            if i+1<length and sig[i] =="0" and sig[i+1] =="0":
                num1-=1
                i-=1
            if num1 <1 :
                flag=False
                break
    if flag==False:
        print("NO")
    else:
        print("YES")