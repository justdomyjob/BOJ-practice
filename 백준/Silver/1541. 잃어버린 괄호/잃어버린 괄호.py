try : standard_input = open("input.txt", "r")  
except:pass

equation = input()

element = []

temp = ""
for char in equation:
    if char!="-" and char!="+":
        temp+=char
    else:
        element.append(temp)
        element.append(char)
        temp=""
element.append(temp)

new_element = []
for e in element:
    for i in range(len(e)):
        if e[i]!="0":
            new_element.append(e[i:])
            break
ans = 0
have_minus = False
for e in new_element:
    if e!="-" and e!="+" and have_minus==False:
        ans+=int(e)
    elif e=="-":
        have_minus=True
    elif e!="-" and e!="+" and have_minus==True:
        ans-=int(e)
print(ans)