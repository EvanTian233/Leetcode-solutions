"""
82. Remove Duplicates from Sorted List II
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        dummy = pre = ListNode(0)
        dummy.next = head
        
        while head and head.next:
            
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next

                head = head.next
                pre.next = head
            else:
                head = head.next
                pre = pre.next                

        return dummy.next
            


