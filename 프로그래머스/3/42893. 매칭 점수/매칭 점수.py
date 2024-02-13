alpha = 'abcdefghijklmnopqrstuvwxyz'
def solution(word, pages):
    word = word.lower()
    pages = [page.lower() for page in pages]
    def get_my_link(page):
        link = "<meta property=\"og:url\" content=\""
        for i in range(len(page)):
            if page[i] == link[0]:
                j = 0
                find = True
                while j<len(link):
                    if page[i+j] != link[j]:
                        find =False
                        break
                    j+=1
                if find:
                    ret = ""
                    idx = 0
                    while page[i+j+idx] != "\"":
                        ret+=page[i+j+idx]
                        idx+=1
                    return ret
    def get_other_link(page):
        link = "<a href=\""
        other_link  = []
        for i in range(len(page)):
            if page[i] == link[0]:
                j = 0
                find = True
                while j<len(link):
                    if page[i+j] != link[j]:
                        find =False
                        break
                    j+=1
                if find:
                    ret = ""
                    idx = 0
                    while page[i+j+idx] != "\"":
                        ret+=page[i+j+idx]
                        idx+=1
                    other_link.append(ret)
        return other_link 
    
    def score(word,page):
        count = 0
        for i in range(len(page)):
            if page[i] == word[0] and page[i-1] not in alpha:
                find = True
                for j in range(len(word)):
                    if i+len(word) >len(page): #다시 확인
                        find = False
                        break
                    if page[i+j] != word[j]:
                        find=False
                        break
                if not find:
                    continue
                elif find:
                    if page[i+len(word)] in alpha:
                        find = False
                if find:
                    count+=1
        return count
    
    dic_score = {}
    for page in pages:
        dic_score[get_my_link(page)] = score(word,page)
    
    

    dic_num_link = {}
    for page in pages:
        other_links = get_other_link(page)
        dic_num_link[get_my_link(page)] = len(other_links)
        

    dic_link_score = {}
    for page in pages:
        other_links = get_other_link(page)
        for other in other_links:
            
            dic_link_score[other] = dic_link_score.get(other,0) + dic_score.get(get_my_link(page),0)/dic_num_link.get(get_my_link(page),1)
            

    page_score = []
    for page in pages:
        my_link = get_my_link(page)
        page_score.append(dic_score.get(my_link,0) + dic_link_score.get(my_link,0))

    a = max(page_score)
    return page_score.index(a)