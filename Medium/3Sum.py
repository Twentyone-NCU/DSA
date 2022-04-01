class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort() # sort the arr to search better

        for i, a in enumerate(nums):
            # first number in the output array
            if i > 0 and a == nums[i-1]: # same value in different position -> skip through this position
                continue

            # second and third number in output array -> two sum tech
            l, r = i+1, len(nums) -1
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0: # too much right value
                    r -=1
                elif threeSum < 0: # too much left value
                    l += 1
                elif threeSum == 0:
                    result.append([a, l, r])
                    
                    l += 1 # keep iterate to find new combination
                    while nums[l] == nums[l-1] and l<r: # pass through the same second value and l<r condition
                        l += 1

        return result
