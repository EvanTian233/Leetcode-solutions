"""
290. Word Pattern
https://leetcode.com/problems/word-pattern/

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false

"""


class Solution:
    def wordPattern(self, pattern: str, word: str) -> bool:
        if not str: return False
        words = word.split(" ")
        if len(pattern) != len(words):
            return False
        
        pattern_map, word_map = {}, {}
        for i in range(len(pattern)):
            if pattern_map.get(pattern[i], -1) != word_map.get(words[i], -1):
                return False
            pattern_map[pattern[i]] = word_map[words[i]] = i
            
        return True
            
            