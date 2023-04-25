from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for l in s:
            if l == "(" or l == "[" or l == "{" : 
                stack.append(l)
            else:
                if not stack:
                    return False
                x = stack.pop()
                if ord(l)-ord(x) > 2 or ord(l)-ord(x) < 0:
                    return False
        if not stack:
            return True
        else:
            return False

A = "()[]{}" 
# A = [7,6,4,3,1]          
a = Solution()
# a.maxProfit(A)
print(a.isValid(A))