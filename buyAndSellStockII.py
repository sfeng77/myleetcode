# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0
        profit = 0
        share = 0
        prices += [0]
        for i in range(0, n):
            if prices[i + 1] > prices[i] and share == 0:
                share = 1
                profit -= prices[i]
            elif:
                prices[i + 1] < prices[i] and share == 1:
                share = 0
                profit += prices[i]
        return profit
