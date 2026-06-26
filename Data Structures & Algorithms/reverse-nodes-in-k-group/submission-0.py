class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy

        while True:
            cur = groupPrev
            count = 0

            # check if k nodes exist
            while cur and count < k:
                cur = cur.next
                count += 1

            if not cur:
                break

            next_group = cur.next
            prev = next_group
            curr = groupPrev.next

            # reverse k nodes
            while curr != next_group:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = prev
            groupPrev = tmp

        return dummy.next
