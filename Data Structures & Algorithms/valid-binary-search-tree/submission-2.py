# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

            def dfs(node, ub, lb):
                if not node:
                    return True
                if node.val>=ub or node.val<=lb:
                    return False
                return dfs(node.left,node.val,lb) and dfs(node.right,ub,node.val)
            
            return dfs(root, float('inf'), float('-inf'))