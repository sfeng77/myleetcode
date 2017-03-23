#  You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#
# Example 1:
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)
#
# Example 2:
# coins = [2], amount = 3
# return -1.
#
# Note:
# You may assume that you have an infinite number of each kind of coin.
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        if amount == 0:
            return 0

        coins.sort()

        try:
            while(coins[0]==0):
                coins.pop(0)
        except IndexError:
            return -1

        n = len(coins)

        MAX = amount / coins[0] + 1
        dp = {}
        dp[0] = 0

        numCoins = 0
        while(numCoins < MAX):
            numCoins += 1
            keys = dp.keys()
            for k in keys:
                for c in coins:
                    if k + c == amount:
                        return numCoins
                    elif k + c > amount:
                        break
                    else:
                        dp[k+c] = min(dp.get(k+c, MAX), numCoins)
            #print dp
        return -1
