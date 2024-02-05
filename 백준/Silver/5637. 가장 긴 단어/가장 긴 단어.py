import re

words = []

while True:
    words.extend(input().split())
    if words[-1] =='E-N-D' :

        break

words = [re.sub('[^a-zA-Z-]','',x.lower()) for x in words ]
words.sort(key =lambda x :  len(x),reverse = True)
print(words[0].lower())