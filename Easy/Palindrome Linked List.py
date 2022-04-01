# Definition for singly -linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val= val
        self.next= next


# Solution for Space O(n) -> Extra array
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nums = []  # extra arr to put in the value

        while head:
            nums.append(head.val)
            head = head.next

        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] != nums[r]: # corresponding head & end
                return False

            l += 1
            r -= 1

        return True

# Solution for Space O(1) -> Fast & Slow pointer, reverse linked list
class Solution:
    def isPalindromeReverse(self, head: ListNode) -> bool:
        fast_pointer = head
        slow_pointer = head

        # find middle (slow)
        while fast_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

        # reverse second half
        prev = None
        while slow_pointer:
            tmp = slow_pointer.next
            slow_pointer.next = prev
            pre = slow_pointer
            slow_pointer = tmp


        # check palindrome
        left, right = head, prev
        while right: # right pointer will eventually shift to the init condition, which is prev = None (line 39)
            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next

        return True
