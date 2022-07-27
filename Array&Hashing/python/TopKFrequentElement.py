"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Hint:
    create an array lens equal to nums.

"""

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pass
#%%
nums = [1,1,1,2,2,3]
k = 2

freq = [ [] ] * len(nums)

for i in nums:
    num = nums.count(i)
    print(num)

    freq[num].append(i)