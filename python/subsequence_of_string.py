from typing import List, Optional

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # i = 0
        # for j in range(len(t)):
        #     if i == len(s):
        #         return True
        #     if t[j] == s[i]:
        #         i += 1
        # return i == len(s)
        i = 0
        j = 0
        for j in range(len(t)):
            if s[i] == t[j]:
                i = i+1
        if s[i]:
            return False
        return True


s = "acb"
t = "ahbgdc"
a = Solution()
# a.replaceElements(arr)
print(a.isSubsequence(s,t))