# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        if not root:
            return 'N'

        dq = deque([root])

        while dq:
            node = dq.popleft()
            if not node:
                res.append('N')
            else:       
                res.append(str(node.val))
                dq.append(node.left)
                dq.append(node.right)

        return ','.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split(',')  
        if arr[0]=='N':
            return None      
        root = TreeNode(int(arr[0]))

        i=1
        dq = deque([root])
        n = len(arr)
        
        while dq:
            node = dq.popleft()
            if i<n and arr[i] != 'N':
                node.left = TreeNode(int(arr[i]))
                dq.append(node.left)
            i+=1
            if i<n and arr[i] != 'N':
                node.right = TreeNode(int(arr[i]))
                dq.append(node.right)
            i+=1
            
        
        return root




            
            

















