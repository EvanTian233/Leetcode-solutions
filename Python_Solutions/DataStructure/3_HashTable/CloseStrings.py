"""
1657. Determine if Two Strings Are Close
https://leetcode.com/problems/determine-if-two-strings-are-close/

Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

 

Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

"""

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        l1, l2 = len(word1), len(word2)
        
        if l1 != l2:    return 0     #if lengths not match then reject
        
        unique_1 = Counter(word1)     #count freq {'a': 1, 'b': 2}
        unique_2 = Counter(word2)
        
		#now, check if each character is present in both words
        for ch in unique_1.keys():
            if ch not in unique_2.keys():
                return 0 
		#okay, so each charater is present now check if each character's freq is also same
		# okay case is {'a': 5, 'b': 2, 'c': 2}
		# Not okay case is {'a': 3, 'b': 4, 'c': 2}  because even thogh each
		# character is present and total char count is also same still chars are not interchangeble
        freq1 = Counter(unique_1.values()) # count freq of each freq 
        freq2 = Counter(unique_2.values())
        
		# check freq counts
        for f, v in freq1.items():
            if freq2[f] != v:
                return 0
        
        return 1