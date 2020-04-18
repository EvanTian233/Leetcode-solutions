"""
203. Remove Linked List Elements
https://leetcode.com/problems/remove-linked-list-elements/

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        dummy_head = ListNode(-1)
        dummy_head.next = head
        
        current_node = dummy_head
        while current_node.next != None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
                
        return dummy_head.next

    def removeElements2(self, head: ListNode, val: int) -> ListNode:
        # Recursion
        if not head:
            return None
        if head.val == val:
            head = self.removeElements(head.next, val)
        else:
            head.next = self.removeElements(head.next, val)
        
        return head
        
        
        
 