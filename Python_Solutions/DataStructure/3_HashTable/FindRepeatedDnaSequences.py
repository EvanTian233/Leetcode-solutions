"""
187. Repeated DNA Sequences
https://leetcode.com/problems/repeated-dna-sequences/

All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T', for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]


"""

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        cnt = defaultdict(int)
        for i in range(n - 9):
            cnt[s[i:i+10]] += 1
        
        print(cnt)

        ans = []
        for key, value in cnt.items():
            if value >= 2: # Found a string that occurs more than once
                ans.append(key)
        return ans

