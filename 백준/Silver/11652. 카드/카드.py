n = int(input())
dic={}
for _ in range(n):
    a = int(input())
    dic[a] = dic.get(a,0) + 1
sorted_dic = sorted(dic.items(), key = lambda x:(-x[1],x[0]))
print(sorted_dic[0][0])