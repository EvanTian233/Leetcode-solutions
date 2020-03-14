



class ReverseLinkedList {
    public ListNode reverseList(ListNode head) {
        // Iterative
        ListNode prev = null;
        ListNode curr = head;
        while(curr != null){
            ListNode nextTemp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = nextTemp;
            
        }
        return prev;
    }

    public ListNode reverseList2(ListNode head) {
        // Recursive
        if (head == null || head.next == null) return head;
        ListNode p = reverseList(head.next);
        head.next.next = head;
        head.next = null;
        return p;
    }
}