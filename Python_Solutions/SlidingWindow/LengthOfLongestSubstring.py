"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

class LengthOfLongestSubstring:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        max_size = 1
        start, end = 0, 1
        char_set = set(s[start])

        while start < len(s) and end < len(s):
            if s[end] in char_set:
                char_set.remove(s[start])
                start += 1
            else:
                char_set.add(s[end])
                end += 1
            max_size = max(max_size, end - start)
        return max_size
        
        
        