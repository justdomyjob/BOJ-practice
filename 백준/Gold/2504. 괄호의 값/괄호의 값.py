string = input()

def rec(s):
    if s == "()":
        return 2
    if s == "[]":
        return 3
    c = case(s)
    if c==1:
        if s[0]=="(":
            return 2* rec(s[1:-1])
        else:
            return 3 * rec(s[1:-1])
    else:
        return rec(s[:c[1]+1]) + rec(s[c[1]+1:])

def case(s):
    num1,num2= 0,0
    if s[0]=="(":
        for i in range(len(s)):
            if s[i] == "(":
                num1+=1
            elif s[i]== ")":
                num2+=1
            if num1==num2:
                if i==len(s)-1:
                    return 1
                else:
                    return 2,i
    elif s[0]=="[":
        for i in range(len(s)):
            if s[i] == "[":
                num1+=1
            elif s[i]== "]":
                num2+=1
            if num1==num2:
                if i==len(s)-1:
                    return 1
                else:
                    return 2,i
try:
    print(rec(string))
except:
    print(0)