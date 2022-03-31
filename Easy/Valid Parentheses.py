class Solution:
    def isValid(self, s: str) -> bool: #Time, Space -> O(n)
        stack = [] # create a stack data structure
        closeToOpen = {")": "(", "]": "[", "}": "{"} # hash map for correspond. Note: from last

        for char in s:
            if char in closeToOpen: # search the key (closing char) of hash map
                if stack and stack[-1] == closeToOpen[char]: # check the stack is not null & last ele in stack equal to the hash map value
                    stack.pop()
                else:
                    return False

            else:
                stack.append(char) # if not match key in hast map, add the open char in stack

        return True if not stack else False # True if stack is empty(null)