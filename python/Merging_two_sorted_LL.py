from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            third = last = list1
            list1 = list1.next
            last.next = None
        else:
            third = last = list2
            list2 = list2.next
            last.next = None
        while list1 and list2:
            if list1.val < list2.val:
                last.next = list1
                last = list1
                list1 = list1.next
                last.next = None
            else:
                last.next = list2
                last = list2
                list2 = list2.next
                last.next = None
        if list1:
            last.next = list1
        else:
            last.next = list2

        return third
    
class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p = q = head
        while True:
            q = q.next
            p = p.next
            if p.next:
                p = p.next
            if not p and not q and p==q:
                break
        if p==q:
            return True
        return False 

head1 = ListNode(1, ListNode(2, ListNode(4)))
head2 = ListNode(1, ListNode(3, ListNode(4)))        
a = Solution()
merged_head = a.mergeTwoLists(head1,head2)
while merged_head:
    print(merged_head.val, end=' ')
    merged_head = merged_head.next
