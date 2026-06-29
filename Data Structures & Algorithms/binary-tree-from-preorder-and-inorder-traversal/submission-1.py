# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def dfs(preorder, inorder):
            if not preorder or not inorder:
                return None
            node = TreeNode(preorder[0])     
            root_index_in = inorder.index(preorder[0])
            node.left = dfs(preorder[1:], inorder[:root_index_in])
            node.right = dfs(preorder[len(inorder[:root_index_in])+1:], inorder[root_index_in+1:])
            return node

        return dfs(preorder, inorder)

