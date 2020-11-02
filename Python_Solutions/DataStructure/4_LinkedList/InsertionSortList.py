"""
147. Insertion Sort List
https://leetcode.com/problems/insertion-sort-list/

Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        
        
        dummyHead = ListNode(0)
        dummyHead.next = nodeToInsert = head
        
        while head and head.next:
            if head.val > head.next.val:
                # Locate nodeToInsert.
                nodeToInsert = head.next
                # Locate nodeToInsertPre.
                nodeToInsertPre = dummyHead
                while nodeToInsertPre.next.val < nodeToInsert.val:
                    nodeToInsertPre = nodeToInsertPre.next
                    
                head.next = nodeToInsert.next
                # Insert nodeToInsert between nodeToInsertPre and nodeToInsertPre.next.
                nodeToInsert.next = nodeToInsertPre.next
                nodeToInsertPre.next = nodeToInsert
            else:
                head = head.next
            
        return dummyHead.next