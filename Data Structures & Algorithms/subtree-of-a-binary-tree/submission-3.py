# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p,q)->bool:
            if not p and not q:
                return True
            if (not p and q) or (not q and p):
                return False
            if p.val!=q.val:
                return False
            return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
        
        def dfs(p,q)->bool:
            if not p:
                return False
            if isSameTree(p,q):
                return True
            else:
                return dfs(p.left,q) or dfs(p.right,q)
        
        return dfs(root,subRoot)
