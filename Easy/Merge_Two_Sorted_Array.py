class Solution:
    def merge(self, nums1: list[int], m:int, nums2: list[int], n:int) -> None:
        # last index of nums1
        last = m + n -1 

        # merge in reverse order
        while m > 0 and n > 0: # check if list null
            if nums1[m-1] > nums2[n-1]: # Cause index start base 0
                nums1[last] = nums1[m]
                m -= 1 # update nums1 pointer

            else: # nums1 <= nums2
                nums1[last] = nums2[n]
                n -= 1 # update nums2 pointer

            last -= 1 # update insert index after a loop
        
        # fill nums1 with leftover nums2 elements
        while n > 0:
            # insert reverse order with nums2 into nums1
            nums1[last] = nums2[n]
            n -= 1
            last -= 1