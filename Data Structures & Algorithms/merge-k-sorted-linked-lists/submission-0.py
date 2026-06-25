# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n=len(lists)
        dummyhead=cur=ListNode(0)
        minheap=[]
        heapq.heapify(minheap)
        count=0

        for l in lists:
            heapq.heappush(minheap, [l.val,count,l])
            count+=1

        while minheap:
            val,_, node = heapq.heappop(minheap)
            cur.next = ListNode(val)
            cur = cur.next
            node = node.next
            if node:
                heapq.heappush(minheap, [node.val,count,node])
            count+=1
        
        return dummyhead.next

