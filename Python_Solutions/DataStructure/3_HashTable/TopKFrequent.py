"""
347. Top K Frequent Elements

https://leetcode.com/problems/top-k-frequent-elements/

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

"""

class TopKFrequent:
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        
        # Counter({1: 3, 2: 2, 3: 1})

        return sorted(count.keys(), key=count.get, reverse=True)[:k]
        #return heapq.nlargest(k, count.keys(), key = count.get)
               