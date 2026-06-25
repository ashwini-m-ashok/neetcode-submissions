class ListNode:
    def __init__(self, key:int,val=0,next=None,prev=None):
        self.val=val
        self.next = next
        self.prev = prev
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.size=capacity
        self.cache = dict()
        self.head=ListNode(0)
        self.tail=ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, remove_node):
        next_node = remove_node.next
        prev = remove_node.prev
        prev.next =next_node
        next_node.prev = prev

    def _add(self,node:Node):
        prev = self.tail.prev
        prev.next=node
        node.prev=prev
        node.next=self.tail
        self.tail.prev=node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._add(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        new_node = ListNode(key)
        new_node.val = value

        self._add(new_node)
        self.cache[key] = new_node

        if len(self.cache) > self.size:
            node = self.head.next
            self._remove(node)
            del self.cache[node.key]
