##
from typing import List
import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        cur_max = 0
        max_till_now = -math.inf

        for i in nums:
            cur_max = max(i, cur_max+i)
            max_till_now = max(cur_max, max_till_now)

        return max_till_now
        

##
nums = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()

s.maxSubArray(nums)
