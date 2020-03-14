/*

234. Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true


 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class PalindromLinkedList {
    public boolean isPalindrome(ListNode head) {
        ListNode fast = head, slow = head;
        while (fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        if(fast != null){
            slow = slow.next;
        }
        slow = reverse(slow);
        fast = head;
        
        while (slow != null){
            if (fast.val != slow.val){
                return false;
            }
            fast = fast.next;
            slow = slow.next;
        }
        return true;
    }
    
    public ListNode reverse(ListNode head){
        ListNode prev = null;
        while(head != null){
            ListNode tempNode = head.next;
            head.next = prev;
            prev = head;
            head = tempNode;
        }
        return prev;
    }
    
}

