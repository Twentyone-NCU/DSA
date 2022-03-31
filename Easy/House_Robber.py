class Solution:
        def rob(self, nums: list[int]) -> list:
            rob1, rob2 = 0, 0 # the maintain sum of last two max we could rob from

            for n in nums:
                # example of array = [rob1, rob2, n, n+1, ...]
                temp = max(n+rob1, rob2) # Selection of rob n element or not

                # iterate next recursion
                rob1 = rob2 # push forward to rob2 position
                rob2 = temp # the max choice of the n position

            return rob2 # Because at the end rob2 is the end of the entire array element
