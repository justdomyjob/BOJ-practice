dic = {}
for i in range(1,27):
    dic[chr(i+ord("A")-1)] = i
    
def solution(msg):
    end_num = 27
    index = []
    cur = 0
    while cur < len(msg):
        long_string = find(msg,cur)  #2
        index.append(dic[long_string]) #3
        cur+= len(long_string)  #3
        if cur<len(msg): #4
            new_word = long_string + msg[cur]
            dic[new_word] = end_num
            end_num+=1
    return index

def find(msg,cur):
    for i in range(len(msg), cur-1,-1):
        if msg[cur:i] in dic:
            return msg[cur:i]
