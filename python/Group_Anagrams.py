from typing import List, Optional

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num1 = [None]*2*n
        for i in range(len(nums)):
            num1[i] = nums[i]
        for y in range(len(nums)):
             num1[n] = nums[y]
             n = n+1
        return num1
    

nums = [1,2,1]
a = Solution()
print(a.getConcatenation(nums))