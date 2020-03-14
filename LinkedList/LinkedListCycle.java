/*

Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
*/

public class LinkedListCycle {
    public boolean hasCycle(ListNode head) {
        // Hash set
        Set<ListNode> nodeSeen = new HashSet<>();
        while (head != null){
            if(nodeSeen.contains(head)){
                return true;
            }else{
                nodeSeen.add(head);
            }
            head = head.next;
        }
        return false;
    }
    public boolean hasCycle(ListNode head) {
        // Two pointers
        if (head == null || head.next == null) {
            return false;
        }
        ListNode slow = head;
        ListNode fast = head.next;
        while (slow != fast) {
            if (fast == null || fast.next == null) {
                return false;
            }
            slow = slow.next;
            fast = fast.next.next;
        }
        return true;
    }
}