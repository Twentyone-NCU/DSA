class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        total_length = len(nums1) + len(nums2)
        half = total_length // 2

        # to make sure A is the smallest length -> faster search for time complexity
        # Time -> O(log (min(m, n)))
        if len(B) < len(A):
            A, B = B, A 


        l, r = 0, len(A)-1
        while True:
            i = (l + r) // 2 # find middle value of A
            j = half - i -2  # B, -2 because two index base on 0

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i+1] if (i+1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright= B[j+1] if (j+1) < len(B) else float("infinity")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total_length % 2 == 1:
                    return min(Aright, Bright) 

                # even
                return max(Aleft, Bleft) + min(Aright, Bright) / 2

            elif Aleft > Bright:
                r = i-1

            else:
                l = i+1