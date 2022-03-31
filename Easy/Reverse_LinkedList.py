# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

class Solution:
    # Iteratively: T->O(n), M->O(1)
    def reverseList_Iteratively(self, head: ListNode) -> ListNode:
        # set to pointer to pre & current node
        prev, curr = None, head

        while curr: # check if current reach to null
            temp = curr.next # temp value to shift
            curr.next = prev # reverse the pointer

            # shift the pointer to next node
            prev = curr
            curr = temp

        return prev

    # Recursively: T->O(n), M->O(n)
    def reverseList_Recursively(self, head: ListNode) -> ListNode:
        # base case: one node
        if not head: # check the head is null
            return None

        newHead = head # maintain the new head
        if head.next: # check if there is still node in head.next
            # if the function still return sth: check the original linked list's last node -> update the newHead to original linked list'slast node
            newHead = self.reverseList_Recursively(head.next) 
            # reverse the head next node's pointer to head -> reverse the pointer
            head.next.next = head

        # tail pointer to Null
        head.next = None

        return newHead