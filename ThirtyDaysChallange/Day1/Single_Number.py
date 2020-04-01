class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Set
        seen = set()
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                seen.remove(i)
        return seen.pop()

    def singleNumber2(self, nums: List[int]) -> int:
        # Bit XOR
        ans = 0
        for num in nums:
            ans ^= num
        return ans
