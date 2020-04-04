"""
387. First Unique Character in a String
https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

"""


from collections import Counter

class FirstUniqChar:
    def firstUniqChar(self, s: str) -> int:
        # Counter -> fast
    	for i,j in Counter(s).items(): 
    		if j == 1: return(s.index(i))
    	return -1
    
    def firstUniqChar2(self, s: str) -> int:
        # Dict
        d = {}
        for l in s:
            if l not in d: d[l] = 1
            else: d[l] +=1
        
        index = -1
        for i, char in enumerate(s):
            if d[char] == 1:
                index = i
                break
        return index
        
        

