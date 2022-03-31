class Solution:
    def climbStairs(self, n: int) -> int:
        # base case: last stair, last stair & pre-stair
        one, two = 1, 1


        for i in range(n-1):
            temp = one # pre store in temp var to update
            
            # update position
            one = one + two
            two = temp # should be two = one(pointer --> temp)

        return one # one is the finally last element of array