from typing import List, Optional

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
    #easy method:
        # words = s.split()
        # return len(words[-1])
    #difficult method:
        i,length = len(s)-1,0
        while s[i] == " ":
            i-=1
        while i>=0 and s[i] != " ":
            length += 1
            i-=1
        return length

s = "Hello World"
a = Solution()
# a.replaceElements(arr)
print(a.lengthOfLastWord(s))