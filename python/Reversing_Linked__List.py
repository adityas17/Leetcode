from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        q = r = None
        p = head
        while p:
            r = q
            q = p
            p = p.next
            q.next = r
        return q


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))       
a = Solution()
reversed_head = a.reverseList(head)
while reversed_head:
    print(reversed_head.val, end=' ')
    reversed_head = reversed_head.next
