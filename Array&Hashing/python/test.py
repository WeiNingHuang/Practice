# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for i in nums:
            if i not in seen:
                seen[i] = 1
            else:
                return True

        return False
#%%

# Test Case
TestCase = [[1,1,1,3,3,4,3,2,4,2], [1,2,3,1], [1,2,3,4]]
s = Solution()

for nums in TestCase:
    print(s.containsDuplicate(nums))

