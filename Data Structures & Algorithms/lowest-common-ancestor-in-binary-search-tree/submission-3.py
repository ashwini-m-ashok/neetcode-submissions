# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(node):
            if (p.val<node.val and node.val<q.val) or  (q.val<node.val and node.val<p.val):
                return node
            elif node.val==p.val or node.val==q.val:
                return node
            elif node.val>p.val and node.val>q.val:
                return dfs(node.left)
            elif node.val<p.val and node.val<q.val:
                return dfs(node.right)
        
        return dfs(root)