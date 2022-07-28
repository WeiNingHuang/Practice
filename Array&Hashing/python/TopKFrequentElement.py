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
nums = [8,8,8,6,6,6,5]
k = 2

freq = [ [] for i in range(len(nums) + 1) ] 

count = {}

for i in nums:
    count[i] = 1+count.get(i, 0)

for k, v in count.items():
    freq[v].append(k)

res = []

for i in range(len(nums) - 1 ,0, -1):
    for n in freq[i]:
        res.append(n)
        if len(res) ==k:
            print(res)
            break
