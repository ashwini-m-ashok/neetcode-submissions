# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        
        cur = slow.next
        prev=None
        slow.next = None

        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        
        second_head = prev
        cur = head

        while cur and second_head:
            next_node = cur.next
            second_next_node = second_head.next
            cur.next = second_head
            second_head.next = next_node
            cur = next_node
            second_head = second_next_node
        







