from typing import List, Optional

class Solution:
    # brute force
    def replaceElements2(self, arr: List[int]) -> List[int]:
        n = len(arr)
        arr2 = [None]*n
        # l,r = 0,1
        # max = arr[1]
        # # print(max)
        # while l<n:
        #     z = r
        max = 0
        z=0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[j] >= max:
                    max = arr[j]
            arr2[z] = max
            z=z+1
            max = -1
        return arr2
    
    # optimal solution
    def replaceElements(self, arr: List[int]) -> List[int]:
        rigthmax = -1
        for i in range(len(arr)-1,-1,-1):
            newMax = max(rigthmax,arr[i])
            arr[i] = rigthmax
            rigthmax = newMax

        return arr


arr = [17,18,5,4,6,1]
a = Solution()
# a.replaceElements(arr)
print(a.replaceElements(arr))