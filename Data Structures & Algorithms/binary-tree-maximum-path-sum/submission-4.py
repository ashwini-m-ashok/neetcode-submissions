# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def dfs(node)->int:
            if not node:
                return 0
            left_path_sum = max(dfs(node.left),0)
            right_path_sum = max(dfs(node.right),0)
            
            cur_sum=node.val+left_path_sum+right_path_sum
            self.max_sum = max(self.max_sum, cur_sum)
            
            return max(left_path_sum,right_path_sum)+node.val
            
        
        dfs(root)
        return self.max_sum 
