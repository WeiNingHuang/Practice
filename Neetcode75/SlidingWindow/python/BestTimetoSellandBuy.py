from typing import List
#%%
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 # left = buy
        right = 1 # right = sell
        max_profit = 0

        while right != len(prices):
            if prices[left] > prices[right] :
                left = right
            else:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            right += 1

#%%

        




