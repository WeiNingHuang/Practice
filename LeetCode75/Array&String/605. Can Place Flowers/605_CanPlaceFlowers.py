"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's,
where 0 means empty and 1 means not empty, and an integer n,
return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
"""

from typing import List

##
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        pass


##
flowerbed = [1, 0, 0, 0, 1]
n = 1

flower_loc = []

for ind, val in enumerate(flowerbed):
    if val == 1:
        flower_loc.append(ind)
