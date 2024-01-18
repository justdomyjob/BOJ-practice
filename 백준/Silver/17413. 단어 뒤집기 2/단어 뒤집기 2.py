from collections import deque

string = input()
stack = deque()

i = 0

def reverseAndNext():
    global i
    while i<len(string) and string[i] != " " and string[i] !="<":
        stack.append(string[i])
        i+=1
    while stack:
        print(stack.pop(), end="")

def justAndNext():
    global i
    while i < len(string) and string[i] != ">":
        print(string[i], end="")
        i += 1
    print(">", end="")
    i += 1

while i<len(string):
    if string[i]==" ":
        print(string[i], end ="")
        i+=1
    elif string[i]=="<":
        justAndNext()
    else:
        reverseAndNext()
