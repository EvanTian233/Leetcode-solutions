"""
138. Copy List with Random Pointer

https://leetcode.com/problems/copy-list-with-random-pointer/

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class CopyRandomList:
    
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic = dict()
        m = n = head
        while m:
            dic[m] = Node(m.val)
            m = m.next
        while n:
            dic[n].next = dic.get(n.next)
            dic[n].random = dic.get(n.random)
            n = n.next
        return dic.get(head)
      
        

    def copyRandomList2(self, head: 'Node') -> 'Node':
        """dict with old Nodes as keys and new Nodes as values. 
        Doing so allows us to create node's next and random as we iterate through the list from head to tail. 
        Otherwise, we need to go through the list backwards.
        defaultdict() is an efficient way of handling missing keys """ 
        map_new = collections.defaultdict(lambda: Node(None, None, None))
        map_new[None] = None # if a node's next or random is None, their value will be None but not a new Node, doing so removes the if-else check in the while loop
        
        nd_old = head
        while nd_old:
            map_new[nd_old].val = nd_old.val
            map_new[nd_old].next = map_new[nd_old.next]
            map_new[nd_old].random = map_new[nd_old.random]
            nd_old = nd_old.next
        return map_new[head]

