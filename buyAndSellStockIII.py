# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
#
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0
        minPrice = prices[0]
        profit = 0
        profitLeft = [0] * n
        for i in range(1,n):
            profit = max(profit, prices[i] - minPrice)
            minPrice = min(prices[i], minPrice)
            profitLeft[i] = profit
        if n < 4:
            return profit
        profitRight = [0] * (n+1)
        maxPrice = prices[n-1]
        profit = 0
        for i in range(n-2, 0, -1):
            profit = max(profit, maxPrice - prices[i])
            maxPrice = max(prices[i], maxPrice)
            profitRight[i] = profit
        profit = 0
        for i in range(n):
            profit = max(profit, profitLeft[i] + profitRight[i+1])
        return profit
