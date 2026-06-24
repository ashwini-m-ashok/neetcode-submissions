# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return head
        fast,slow=head,head

        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next

        cur,prev=slow.next,None
        slow.next=None

        while cur:
            next_node = cur.next
            cur.next = prev
            prev=cur
            cur=next_node
        
        l2=prev
        l1=head

        while l2:
            l1next = l1.next
            l2next = l2.next

            l1.next=l2
            l2.next=l1next

            l1=l1next
            l2=l2next
        
