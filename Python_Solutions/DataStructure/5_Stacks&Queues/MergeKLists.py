"""
23. Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []


"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        pre = cur = ListNode(0)
           
        heap = []
        for i in range(len(lists)):
            if lists[i]: 
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
                
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            cur.next = node[2]  
            cur = cur.next
            
            if cur.next:
                heapq.heappush(heap, (cur.next.val, idx, cur.next))

        return pre.next