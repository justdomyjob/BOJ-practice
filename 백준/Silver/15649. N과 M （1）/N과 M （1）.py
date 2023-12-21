import copy


try : standard_input = open("input.txt", "r")  
except:pass

N, M = map(int,input().split())

def recursive(num_list,M):
    ret = []
    if M ==1:
        for num in num_list:
            ret.append(str(num))
        return ret       
    for num in num_list:
        new_list = copy.deepcopy(num_list)
        new_list.remove(num)
        for _list in recursive(new_list,M-1):
            ret.append(str(num) + " " + _list)
    return ret
for e in recursive([i+1 for i in range(N)],M):
    print(e)
