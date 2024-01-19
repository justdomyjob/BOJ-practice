import copy
import sys
from collections import Counter, deque

N = int(input())
words = []
for _ in range(N):
    words.append(sys.stdin.readline().rstrip())

def isPalindrome(word):
    for i in range(len(word)//2):
        if word[i]!=word[-(i+1)]:
            return False
    return True

def isPseudoPalindrome(word):
    for i in range(len(word)//2):
        sameWord = copy.deepcopy(word)
        if word[i]!=word[-(i+1)]:
            word1 = word[:i] + word[i+1:]
            word2 = word[:len(word)-(i+1)] + word[len(word)-(i+1)+1:]
            if isPalindrome(word1) or isPalindrome(word2):
                return True
            else:
                return False
    return True
for word in words:
    if isPalindrome(word):
        print(0)
    elif isPseudoPalindrome(word):
        print(1)
    else:
        print(2)
