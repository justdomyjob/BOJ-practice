num = input()


if len(num)<=1:
    print(0)
    exit(0)

before = num[0]
count = 0
for n in num[1:]:
    if n==before:
        continue
    else:
        count+=1
        before = n
print((count+1)//2)