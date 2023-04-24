from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            myMap = {}
            for ch in s:
                myMap[ch] = 1 + myMap.get(ch,0)
            
            for n in t:
                if n in myMap:
                    myMap[n] = myMap.get(n) - 1
                else:
                    return False

            if all(value == 0 for value in myMap.values()):
                return True


s = "anagram"
t = "nagaram"
a = Solution()
print(a.isAnagram(s,t))
            
            