from typing import List, Optional

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        while l<=r:
            mid = (l+r)//2
            x = guess(mid)
            if x==0:
                return mid
            elif x==-1:
                r = mid-1
            else:
                l = mid+1