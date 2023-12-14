try : standard_input = open("input.txt", "r")  
except:pass

string = input()
q = int(input())
sum= [[0] for _ in range(26)]
for alphabet in string:
    for i in range(26):
        if ord(alphabet) - 97 ==i:
            sum[i].append(sum[i][-1]+1)
        else:
            sum[i].append(sum[i][-1])
for _ in range(q):
    a, i, j = input().split()
    i, j =int(i), int(j)
    print(sum[ord(a)-97][j+1]-sum[ord(a)-97][i])