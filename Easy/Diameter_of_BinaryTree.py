# Definition for a binary tree node
from logging import root
from turtle import left, right


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution: #Time->O(n)
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = [0] # global var for nesting loop

        def dfs(root): # dfs for the current counting root
            if not root: # check the node is note null
                return -1  # default of height for null --> helping to count diameter

            left = dfs(root=root.left)
            right = dfs(root=root.right)

            res[0] = max(res[0], 2 + left + right) # return the maximum diameter

            return 1 + max(left, right) # the height of the searching node

        dfs(root= root)
        
        return res[0] # return the maximum diameter