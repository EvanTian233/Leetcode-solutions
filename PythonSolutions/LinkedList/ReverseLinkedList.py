"""
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev            


    def reverseList2(self, head: ListNode) -> ListNode:
        return self._reverse(head)
    
    def _reverse(self, node, prev = None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)
    
    
    