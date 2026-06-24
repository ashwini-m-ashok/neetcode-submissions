# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1,l2=list1,list2
        dummyhead = cur= ListNode(0)
        
        dummyhead.next = cur
        
        while l1 and l2:
            l1val = l1.val 
            l2val = l2.val
            if l1val<l2val:
                new_node_val = l1val
                l1 = l1.next
            else:
                new_node_val = l2val
                l2 = l2.next
            
            cur.next = ListNode(new_node_val)
            cur = cur.next

        cur.next = l1 if l1 else l2

        return dummyhead.next

