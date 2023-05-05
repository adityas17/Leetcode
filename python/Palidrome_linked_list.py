from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        p = head
        mylist = []
        while p:
            mylist.append(p.val)
            p = p.next
        i,j = 0,len(mylist)-1
        while i<j:
            if mylist[i]!=mylist[j]:
                return False
            i+=1
            j-=1
        return True


head1 = ListNode(1, ListNode(2))
a = Solution()
print(a.isPalindrome(head1))