"""
188. Best Time to Buy and Sell Stock IV
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Notice that you may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

"""


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        
        if k >= len(prices) // 2:
            return sum(
                x-y
                for x, y in zip(prices[1:], prices[:-1])
                if x > y
            )
        
        profits = [0] * len(prices)
        for j in range(k):
            preprofit = 0
            for i in range(1, len(prices)):
                
                profit = prices[i] - prices[i-1]
                preprofit = max(preprofit + profit, profits[i])
                profits[i] = max(profits[i-1], preprofit)
                
        return profits[-1]


