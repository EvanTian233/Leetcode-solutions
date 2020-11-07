"""
445. Add Two Numbers II
https://leetcode.com/problems/add-two-numbers-ii/

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = n2 = 0
        
        while l1:
            n1, l1 = n1 * 10 + l1.val, l1.next
        while l2:
            n2, l2 = n2 * 10 + l2.val, l2.next
            
        total = str(n1 + n2)
        pre = dummy = ListNode(0)
        
        for a in total:
            pre.next = pre = ListNode(int(a))
            
        return dummy.next
        

