N = int(input())
M = int(input())
string = input()

first2N = string[:N*2]

length = 1
for i in range(-2,-(2*N+1),-1):
    if first2N[i+1] == first2N[i]:
        break
    elif first2N[i+1] != first2N[i]:
        length+=1


count = 0
for i in range(2*N, M):
    if length==N*2 and string[i]=="I" and string[i-1] =="O":
        count+=1
    elif string[i] == string[i-1]:
        length =1
    elif string[i] != string[i - 1] and length < 2*N:
        length+=1
print(count)
