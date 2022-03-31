class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l_pointer, r_pointer = 0, len(numbers-1)
        while l_pointer < r_pointer:
            curSum = numbers[l_pointer] + numbers[r_pointer]

            if curSum > target: # Too big 
                r_pointer -= 1
            elif curSum < target: # Too small
                l_pointer += 1
            else: # equal to target # add 1 because base on 1
                return [l_pointer+1, r_pointer+1] 
