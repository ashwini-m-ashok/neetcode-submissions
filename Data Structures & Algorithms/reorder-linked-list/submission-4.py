# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = list()

        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        
        n = len(nodes)
        res = []
        l=0
        r=n-1

        while l<r:
            nodes[l].next = nodes[r]
            l+=1
            if l>=r:
                break
            nodes[r].next = nodes[l]
            r-=1
        
        nodes[l].next=None







