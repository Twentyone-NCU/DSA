#  Definition of singly-linked list
class ListNode:
    def __init__(self, val= 0, next= None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Avoid edge case -> dummy tech
        dummy = ListNode()
        tail = dummy

        while l1 and l2: # Check link listed are both not empty
            if l1.val < l2.val: # compare node value & add the small value
                tail.next = l1.val 
                l1 = l1.next # Renew l1 pointer
            else:
                tail.next = l2.val
                l2 = l2.next # Renew L2 pointer

            tail = tail.next # Update tail pointer

        # Insert the remaining list
        if l1:
            tail.next = l1
        elif l1:
            tail.next = l2
        
        return dummy.next # function expect ListNode
