from typing import List, Optional

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        mid = 0
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                l = mid+1
            else:
                r = mid-1
        return -1

nums = [-1,0,3,5,9,12]           
a = Solution()
print(a.search(nums,9))