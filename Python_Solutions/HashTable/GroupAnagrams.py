"""
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

"""

class GroupAnagrams:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Using dict
        d = {}
        for w in strs:
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]           # (key, defaultValue)
                                                    # Print([] + [w]+ [w]) -> ['eat', 'eat']
        return list(d.values())
