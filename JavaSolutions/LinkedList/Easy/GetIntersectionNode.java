/*

160. Intersection of Two Linked Lists

https://leetcode.com/problems/intersection-of-two-linked-lists/

 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 * 
*/


public class GetIntersectionNode {

    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        // Hash set
        if(headA == null || headB == null) return null;

        Set<ListNode> nodeSeen = new HashSet<>();
        
        while(headA != null){
            nodeSeen.add(headA);
            headA = headA.next;
        }
        
        while(headB != null){
            if(nodeSeen.contains(headB)){
                return headB;
            }else{
            nodeSeen.add(headB);
            headB = headB.next;
            }
        }
        return null;        
        
    }


    public ListNode getIntersectionNode2(ListNode headA, ListNode headB) {
        // Set as asame start

        int lenA = length(headA), lenB = length(headB);
        // move headA and headB to the same start point
        while (lenA > lenB) {
            headA = headA.next;
            lenA--;
        }
        while (lenA < lenB) {
            headB = headB.next;
            lenB--;
        }
        // find the intersection until end
        while (headA != headB) {
            headA = headA.next;
            headB = headB.next;
        }
        return headA;
    }
    
    private int length(ListNode node) {
        int length = 0;
        while (node != null) {
            node = node.next;
            length++;
        }
        return length;
    }
}
