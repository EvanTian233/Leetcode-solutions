class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                seen.remove(i)
        return seen.pop()
