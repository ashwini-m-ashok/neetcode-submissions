# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def calc_height(node)->int:
            if not node:
                return 0
            return max(calc_height(node.left),calc_height(node.right))+1

        def dfs(node)-> bool:
            if not node:
                return True
            left_h = calc_height(node.left)
            right_h = calc_height(node.right)
            if abs(left_h-right_h)>1:
                return False
            return dfs(node.left) and dfs(node.right)
        
        return dfs(root)

