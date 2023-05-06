from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        prev,curr = dummy,head

        while curr:
            nxt = curr.next

            if curr.val == val:
                prev.next = nxt
            else:
                prev = curr

            curr = nxt
        return dummy.next

            

head1 = head = ListNode(6, ListNode(6, ListNode(6, ListNode(6, ListNode(6, ListNode(4, ListNode(8, ListNode(6)))))))) 
a = Solution()
New = a.removeElements(head1,6)
while New:
    print(New.val, end=' ')
    New = New.next