from typing import List, Optional

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        k = i
        while i < len(nums) - 1:
            if nums[i]==nums[i+1]:
                j = i+1
                k+=1
                while nums[j]==nums[i]:
                    j+=1
                nums[k] = nums[j]
                i = j
            else:
                i+=1
        print(*nums)
        return k+1

nums = [0,0,1,1,1,2,2,3,3,4]        
a = Solution()
print(a.removeDuplicates(nums))
                            
            

