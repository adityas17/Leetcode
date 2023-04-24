from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}

        for n in range(len(nums)):
            if target - nums[n] in myMap:
                return [myMap[target - nums[n]],n]
            else:
                myMap[nums[n]] = n



#A = [2,7,11,15]
A = [3,3]
a = Solution()
print(a.twoSum(A,9))