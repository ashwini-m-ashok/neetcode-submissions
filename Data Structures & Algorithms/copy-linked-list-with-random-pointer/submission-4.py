"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        old_to_new={}

        cur=head

        while cur:
            old_to_new[cur] = Node(cur.val)
            cur=cur.next
        
        for old_node in old_to_new:
            new_node = old_to_new[old_node]
            new_node.next =  old_to_new.get(old_node.next)
            new_node.random =  old_to_new.get(old_node.random)

        return old_to_new[head]

            