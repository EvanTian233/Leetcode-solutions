"""
148. Sort List
https://leetcode.com/problems/sort-list/

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Merge sort
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        fast,slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(second)
        
        return self.merge(l, r)
    
    def merge(self, l, r):
        if not l or not r:
            return l or r
        if l.val > r.val:
            l, r = r, l
            
        # get the return node "head"

        head = pre = l
        l = l.next
        
        while l and r:
            if l.val < r.val:
                pre.next = l
                l = l.next
            else:
                pre.next = r
                r = r.next
            pre = pre.next
        # l and r at least one is None
        pre.next = l or r
        return head
        
        