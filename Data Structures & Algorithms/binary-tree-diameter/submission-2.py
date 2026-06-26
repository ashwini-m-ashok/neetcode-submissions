# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_h=0

        def dfs(node)->int:
            if not node:
                return 0
            left_h = dfs(node.left)
            right_h = dfs(node.right)
            
            max_node_h = left_h+right_h
            self.max_h = max(self.max_h, max_node_h)
            return max(left_h,right_h)+1

        dfs(root)
        return self.max_h