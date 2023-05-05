from typing import List, Optional

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x = strs[0]

        for i in range(1,len(strs)):
            

strs = ["flower","flow","flight"]
a = Solution()
# a.replaceElements(arr)
print(a.longestCommonPrefix(strs))